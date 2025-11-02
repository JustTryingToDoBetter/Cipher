#!/usr/bin/env python3
# ec_password_generator.py
#
# Production-ready implementation of the Project-1 pipeline for COS738:
# - Create a small random noise CSV (for TuringBot input)
# - Deterministically map a memorable password to a numeric seed
# - Generate a pseudo-random stream by iterating an EC cipher function
# - Post-process stream to a uniform distribution
# - Map to printable ASCII and output a strong password (and optionally save)
#
# NOTE: You MUST replace the `ec_formula` implementation with your own
# TuringBot-generated expression (keep the same function signature).
#

#
# Usage (CLI):
#   python ec_password_generator.py --memorable "my weak pwd" --length 24 --out-file ec_strong_password.txt
#
# Security note: This script writes the generated password to a file only if explicitly requested.
# Keep output files secure (file permissions / secure deletion) as required by your security policy.

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import math
import os
import stat
import sys
from typing import Callable, Iterable, List

import numpy as np
from scipy.stats import rankdata

# -----------------------------------------------------------------------------
# Logging configuration
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("ec_password_generator")


# -----------------------------------------------------------------------------
# Configuration constants
# -----------------------------------------------------------------------------
PRINTABLE_START = 33  # '!'
PRINTABLE_END = 126  # '~'
PRINTABLE_RANGE = PRINTABLE_END - PRINTABLE_START + 1

DEFAULT_TURINGBOT_CSV = "turingbot_noise.csv"
DEFAULT_OUT_FILE = "ec_strong_password.txt"


# -----------------------------------------------------------------------------
# Public API functions
# -----------------------------------------------------------------------------
def write_noise_csv(path: str = DEFAULT_TURINGBOT_CSV, count: int = 50) -> None:
    """
    Generate `count` floating-point values in (0,1) and write one per line to `path`.
    Intended for uploading to TuringBot (or similar) to evolve an EC formula.
    Overwrites existing file.
    """
    rng = np.random.default_rng()  # non-deterministic RNG for noise pool generation
    samples = rng.random(count)
    with open(path, "w", encoding="utf-8") as f:
        for v in samples:
            f.write(f"{v:.12f}\n")
    logger.info("Noise CSV written to %s (%d values)", path, count)


def memorable_to_seed_float(memorable: str) -> float:
    """
    Deterministically convert a memorable password string into a float in (0,1).
    Uses SHA-256 -> integer -> scaled float. Stable across platforms and Python runs.
    """
    if not isinstance(memorable, str):
        raise TypeError("memorable must be a string")
    h = hashlib.sha256(memorable.encode("utf-8")).digest()
    # take first 12 bytes -> a 96-bit integer, scale to (0, 1)
    trunc = int.from_bytes(h[:12], "big")
    max_val = (1 << (12 * 8)) - 1
    seed = (trunc + 1) / (max_val + 2)  # avoid exactly 0 or 1
    logger.debug("memorable_to_seed_float: seed=%r", seed)
    return float(seed)


import math

def ec_formula(x: float) -> float:
    """Stable version of your evolved EC formula with safe guards."""

    # ---- Safe math wrappers ----
    def safe_tan(v):
        # wrap input into (-pi/2, pi/2) and avoid infinities
        v = (v + math.pi/2) % math.pi - math.pi/2
        try:
            return math.tan(v)
        except Exception:
            return 0.0

    def safe_atanh(v):
        # clamp input into (-0.999999, 0.999999)
        return math.atanh(max(-0.999999, min(0.999999, v)))

    def safe_div(a, b):
        if abs(b) < 1e-9:
            return 0.0
        return a / b

    # ---- Your evolved cipher (same structure, safer math) ----
    val = (
        0.245247
        - 0.00355652 * safe_tan(x + 0.997621)
        - (2.50253 * safe_tan(x + x + 0.990735))
        + 41.4887
        - (safe_tan(1.99855 + safe_atanh(x)) - 0.996519)
        + safe_div(safe_tan(x + 0.928126), -2.46095)
        * (0.986526 + (safe_atanh(x) - 0.918575))
        * (x - 1.04439 + 2.59159 * x)
        + x * (x + 1)
        + safe_tan(1.42159 + x)
        - safe_tan((-12.2847) * x + (-9.10391) * x)
    )

    # ---- Final clamp: replace NaN or Inf with bounded value ----
    if not np.isfinite(val):
        val = math.tanh(x)  # soft fallback to keep continuity

    return val
def generate_random_stream(
    seed_value: float, length: int, ec_func: Callable[[float], float]
) -> List[float]:
    """
    Iterate the ec_func starting from seed_value to produce `length` floats.
    Returns a list of floats of length `length`.
    """
    if length <= 0:
        raise ValueError("length must be a positive integer")
    if not (0.0 < seed_value < 1.0):
        logger.warning("seed_value is not in (0,1); ec functions may expect this range")
    stream = np.empty(length, dtype=float)
    stream[0] = float(seed_value)
    for i in range(1, length):
        prev = float(stream[i - 1])
        try:
            nxt = float(ec_func(prev))
        except Exception as e:
            logger.exception("ec_func raised an error at iteration %d: %s", i - 1, e)
            raise
        # Guard against NaN/Inf from user-supplied formula
        if not np.isfinite(nxt):
            raise ArithmeticError(
                f"ec_func returned non-finite value at iteration {i}: {nxt!r}"
            )
        stream[i] = nxt
    return stream.tolist()


def transform_to_uniform(input_array: Iterable[float]) -> np.ndarray:
    """
    Convert numeric array to a uniform distribution in [0,1] while preserving order
    (rank-based empirical CDF). Uses scipy.stats.rankdata.
    """
    arr = np.asarray(list(input_array), dtype=float)
    if arr.size == 0:
        return arr
    ranks = rankdata(arr, method="average")  # 1-based ranks
    uniform = (ranks - 1) / (len(arr) - 1) if len(arr) > 1 else np.array([0.5])
    return np.asarray(uniform, dtype=float)


def map_uniform_to_printable(uniform_array: Iterable[float]) -> str:
    """
    Map each value in uniform_array (assumed in [0,1]) to a printable ASCII char
    in the range PRINTABLE_START..PRINTABLE_END inclusive.
    """
    u = np.clip(np.asarray(list(uniform_array), dtype=float), 0.0, 1.0)
    # map 0..1 -> 0..PRINTABLE_RANGE-1 then to ASCII
    indices = np.floor(u * PRINTABLE_RANGE).astype(int) % PRINTABLE_RANGE
    chars = [chr(PRINTABLE_START + idx) for idx in indices]
    return "".join(chars)


def generate_ec_strong_password(
    memorable_password: str, length: int, ec_func: Callable[[float], float]
) -> str:
    """
    Full pipeline to create a deterministic strong password from memorable_password.
    - Convert memorable_password -> float seed
    - Generate stream by iterating ec_func
    - Transform to uniform distribution
    - Map to printable ASCII
    Returns a string of exactly `length` characters.
    """
    if length <= 0:
        raise ValueError("length must be a positive integer")
    seed = memorable_to_seed_float(memorable_password)

    # We need a stream length at least `length`. Use exactly length.
    raw_stream = generate_random_stream(seed, length, ec_func)
    uniform_stream = transform_to_uniform(raw_stream)
    strong = map_uniform_to_printable(uniform_stream)
    if len(strong) != length:
        # sanity check
        raise RuntimeError(
            f"unexpected output length: expected {length}, got {len(strong)}"
        )
    return strong


# -----------------------------------------------------------------------------
# Helper utilities
# -----------------------------------------------------------------------------
def _secure_write_text_file(path: str, content: str, mode: int = 0o600) -> None:
    """
    Write `content` to `path` with file permissions set to `mode` (octal).
    Overwrites existing file.
    """
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    with os.fdopen(os.open(path, flags, mode), "w", encoding="utf-8") as f:
        f.write(content)
    # Ensure permissions (some OS behaviors need explicit chmod)
    os.chmod(path, mode)
    logger.info("Saved output to %s (mode %o)", path, mode)


# -----------------------------------------------------------------------------
# CLI Entrypoint
# -----------------------------------------------------------------------------
def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ec_password_generator",
        description="EC-based deterministic strong password generator (Project 1).",
    )
    parser.add_argument(
        "--memorable",
        "-m",
        type=str,
        required=True,
        help="Memorable weak password (input seed).",
    )
    parser.add_argument(
        "--length",
        "-l",
        type=int,
        required=True,
        help="Desired strong password length (positive integer).",
    )
    parser.add_argument(
        "--out-file",
        "-o",
        type=str,
        default=None,
        help="Optional: write the strong password to a file (secure permissions applied).",
    )
    parser.add_argument(
        "--generate-noise-csv",
        action="store_true",
        help=f"Generate a {DEFAULT_TURINGBOT_CSV} containing 50 random floats for TuringBot.",
    )
    parser.add_argument(
        "--noise-count",
        type=int,
        default=50,
        help="Number of samples to generate in noise CSV if requested (default 50).",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable DEBUG logging.",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv)
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")

    if args.generate_noise_csv:
        write_noise_csv(DEFAULT_TURINGBOT_CSV, count=args.noise_count)
        # If only generating CSV, exit successfully
        if not (args.memorable and args.length):
            return 0

    # Validate ec_formula implemented
    if ec_formula.__doc__ and "NotImplementedError" in ec_formula.__doc__:
        # We cannot reliably detect replacement; attempt a call with seed to see if implemented
        try:
            _ = ec_formula(0.5)
            logger.debug("ec_formula callable with sample input")
        except NotImplementedError:
            logger.error(
                "ec_formula is not implemented. Replace ec_formula() with your TuringBot formula."
            )
            return 2
        except Exception:
            # ec_formula exists but may raise for other reasons; proceed and allow runtime errors to surface
            logger.debug("ec_formula exists but raised on test call", exc_info=True)

    try:
        strong = generate_ec_strong_password(args.memorable, args.length, ec_formula)
    except Exception as e:
        logger.exception("Failed to generate strong password: %s", e)
        return 3

    # Print to stdout (user-visible)
    print(strong)

    if args.out_file:
        # Save with secure permissions (user rw only)
        try:
            _secure_write_text_file(args.out_file, strong + "\n", mode=0o600)
        except Exception as e:
            logger.exception("Failed to write output file: %s", e)
            return 4

    return 0


# -----------------------------------------------------------------------------
# If executed as script
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Keep exit codes meaningful for CI / scripts
    exit_code = main()
    sys.exit(exit_code)
