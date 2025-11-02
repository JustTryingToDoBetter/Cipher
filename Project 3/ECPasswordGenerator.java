import java.io.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.stream.*;

public class ECPasswordGenerator {

    // Printable ASCII range
    private static final int PRINTABLE_START = 33;
    private static final int PRINTABLE_END = 126;
    private static final int PRINTABLE_RANGE = PRINTABLE_END - PRINTABLE_START + 1;

    // --- Utility: deterministic hash-to-float ---
    public static double memorableToSeed(String memorable) throws Exception {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(memorable.getBytes("UTF-8"));

        long value = 0;
        for (int i = 0; i < 12; i++) {
            value = (value << 8) | (hash[i] & 0xFF);
        }
        double maxVal = Math.pow(2, 96) - 1;
        double seed = (value + 1) / (maxVal + 2);
        return seed;
    }

    // --- Safe math wrappers ---
    private static double safeTan(double v) {
        v = (v + Math.PI / 2) % Math.PI - Math.PI / 2;
        return Math.tan(v);
    }

    private static double safeAtanh(double v) {
        v = Math.max(-0.999999, Math.min(0.999999, v));
        return 0.5 * Math.log((1 + v) / (1 - v));
    }

    private static double safeDiv(double a, double b) {
        return Math.abs(b) < 1e-9 ? 0.0 : a / b;
    }

    // --- EC formula (your evolved cipher) ---
    public static double ecFormula(double x) {
        double val;
        try {
            val = 0.245247
                - 0.00355652 * safeTan(x + 0.997621)
                - (2.50253 * safeTan(x + x + 0.990735))
                + 41.4887
                - (safeTan(1.99855 + safeAtanh(x)) - 0.996519)
                + safeDiv(safeTan(x + 0.928126), -2.46095)
                * (0.986526 + (safeAtanh(x) - 0.918575))
                * (x - 1.04439 + 2.59159 * x)
                + x * (x + 1)
                + safeTan(1.42159 + x)
                - safeTan((-12.2847) * x + (-9.10391) * x);
        } catch (Exception e) {
            val = Math.tanh(x);
        }
        if (Double.isNaN(val) || Double.isInfinite(val)) val = Math.tanh(x);
        return val;
    }

    // --- Generate iterative random stream ---
    public static double[] generateStream(double seed, int length) {
        double[] stream = new double[length];
        stream[0] = seed;
        for (int i = 1; i < length; i++) {
            stream[i] = ecFormula(stream[i - 1]);
        }
        return stream;
    }

    // --- Rank-transform to uniform [0,1] ---
    public static double[] transformToUniform(double[] arr) {
        double[] sorted = arr.clone();
        Arrays.sort(sorted);
        double[] uniform = new double[arr.length];
        for (int i = 0; i < arr.length; i++) {
            int rank = Arrays.binarySearch(sorted, arr[i]);
            uniform[i] = (double) rank / (arr.length - 1);
        }
        return uniform;
    }

    // --- Map to printable ASCII ---
    public static String mapToPrintable(double[] uniform) {
        StringBuilder sb = new StringBuilder();
        for (double u : uniform) {
            int idx = (int) Math.floor(u * PRINTABLE_RANGE) % PRINTABLE_RANGE;
            sb.append((char) (PRINTABLE_START + idx));
        }
        return sb.toString();
    }

    // --- Full generator pipeline ---
    public static String generateECPassword(String memorable, int length) throws Exception {
        double seed = memorableToSeed(memorable);
        double[] raw = generateStream(seed, length);
        double[] uniform = transformToUniform(raw);
        return mapToPrintable(uniform);
    }

    // --- CLI test ---
    public static void main(String[] args) throws Exception {
        String memorable = "test123";
        int length = 20;
        String password = generateECPassword(memorable, length);
        System.out.println("Generated Strong Password: " + password);
    }
}
