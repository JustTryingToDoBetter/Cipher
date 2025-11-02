# 🧠 COS738 Cybersecurity — Project 2
## Strong Password Generator GUI using an Evolutionary Computed Cipher

### 📘 Overview
This project forms **Part 2** of the COS738 Specialist Seminar Series assignment by **J.M. Blackledge (2025)**.  
It implements a **Graphical User Interface (GUI)** for a **Strong Password Generator** based on an **Evolutionary Computed Cipher (EC Cipher)** derived from the **TuringBot symbolic regression system**, as discussed in the pre-publication *Application of Evolutionary Computing for Generating Encryption Algorithms using AI-based Code Generation (Blackledge et al., 2025)*.

The GUI provides a user-friendly front-end to the underlying Python program developed in **Project 1**, allowing users to:
- Input a memorable (weak) password,  
- Specify the desired length of a strong password,  
- Generate a deterministic strong password derived from an EC-based nonlinear function,  
- Display and optionally save the result to file.

---

### 🧩 Project Architecture

#### Components
| Component | Description |
|------------|--------------|
| `ec_formula(row)` | The TuringBot-generated nonlinear function that produces the pseudo-random sequence. |
| `generate_random_number_stream(seed, length)` | Iterates the EC function to produce a random number stream from a password-derived seed. |
| `transform_to_uniform()` | Post-processes the stream into a uniform distribution for cryptographic consistency. |
| `generate_ec_strong_password()` | Maps the numeric stream into printable ASCII characters forming a strong password. |
| `GUI.py` | Python Tkinter-based GUI integrating the functions above. |

#### Tools Used
- **Python 3.10+**
- **Tkinter** — GUI development  
- **NumPy** and **SciPy** — Statistical post-processing  
- **Math** — Core nonlinear operations  

---

### 🖥️ GUI Features

**Input Fields:**
- Memorable password (weak password)
- Desired strong password length

**Output Fields:**
- Generated strong password (displayed in window)
- Option to save password pair to `ec_strong_password.txt`

**Example Layout:**
```
+------------------------------------------------------+
|     EC-Based Strong Password Generator               |
+------------------------------------------------------+
| Enter memorable password: [____________________]     |
| Enter desired length:      [____]                    |
|                                                      |
| [Generate Password]                                  |
|                                                      |
| Strong password: [GeneratedPassword123@!]            |
|                                                      |
| [Save to File]     [Exit]                            |
+------------------------------------------------------+
```

---

### ⚙️ How It Works

1. **Input Processing:**  
   The memorable password is converted into a numerical seed by summing normalised ASCII values.

2. **Cipher Generation:**  
   The seed drives the EC nonlinear function (TuringBot-derived) to generate a pseudo-random number stream.

3. **Distribution Transformation:**  
   The generated sequence is normalised to a uniform distribution using statistical ranking.

4. **Password Construction:**  
   Numeric values are mapped into printable ASCII characters to form the final strong password.

5. **Output Handling:**  
   The strong password is displayed in the GUI and optionally written to `ec_strong_password.txt`.

---

### 🧮 Core Evolutionary Cipher Function

```python
def ec_formula(row):
    return 0.432357 + (-0.498752 * math.cos(
        0.594808 * (-4.10993 * math.cosh(row) -
        (0.590558 + math.atanh(math.cos(
        math.tan(math.cos(row / (-0.00153462))) + row * row))))))
```

This equation was generated through **TuringBot symbolic regression** using real noise data from **Random.org**, approximating a chaotic pseudo-random stream.

---

### 🚀 Execution Guide

1. **Install dependencies:**
   ```bash
   pip install numpy scipy
   ```
2. **Run the GUI:**
   ```bash
   python GUI.py
   ```
3. **Generate Password:**
   - Enter your weak password (e.g., `maskiplayground`)
   - Enter desired length (e.g., `16`)
   - Click **Generate Password**

4. **Save Output (optional):**
   Click **Save to File** to store both memorable and strong passwords.

---

### 🧪 Example Run

**Input:**
```
Memorable Password: maskiplayground
Length: 16
```

**Output:**
```
Strong Password: f]3d)E{n9<QjR|Vx
```

**Saved file:**
```
ec_strong_password.txt
-----------------------
Memorable password: maskiplayground
Strong password: f]3d)E{n9<QjR|Vx
```

---

### 📊 Assessment Mapping

| Assessment Criterion | Evidence |
|-----------------------|-----------|
| Functionality (50%) | GUI operates correctly, generates deterministic strong passwords. |
| Code Clarity (25%) | Clean, modular Python code with comments and separation of logic. |
| Explanation (25%) | This README provides full operational and technical context. |

---

### 📚 References

- J.M. Blackledge, R. Kingstone, B. Midgley. *Application of Evolutionary Computing for Generating Encryption Algorithms using AI-based Code Generation*. IntechOpen, 2025.  
- COS738 Assignment Brief, University of the Western Cape (2025).  
- [Random.org](https://www.random.org) — Source of true random number streams.  
- [TuringBot.com](https://turingbot.com) — Symbolic regression AI platform.  

---

### 🧑‍💻 Author
**Student:** Jaydin Morrison  
**Module:** COS738 – Cyber Security  
**Institution:** University of the Western Cape  
**Project:** Part 2 – GUI for EC-Based Strong Password Generator  
**Submission Deadline:** 31 October 2025  
