# COS738 Cybersecurity Assignment – Blackledge (2025)
**Module:** COS738 Cyber Security  
**Lecturer:** Prof. J.M. Blackledge  
**Examiner:** J.M. Blackledge  
**Weighting:** 20%  
**Submission Deadline:** 31 October 2025 @ 17:00 (SAST)

---

## 📘 Project Overview
This assignment is based on the paper *“Application of Evolutionary Computing for Generating Encryption Algorithms using AI-based Code Generation”* by Blackledge, Kingstone, and Midgley (2025), provided in the **Pre-publication.pdf**.  

The overall goal is to develop a software system that:
1. Generates a **unique cipher** using **Evolutionary Computing (EC)** through **TuringBot**.  
2. Builds a **Graphical User Interface (GUI)** to create and display strong passwords generated using that cipher.  
3. **Translates** the final Python implementation into **Java**, ensuring equivalent logic and GUI functionality.

---

## 🧩 Project Structure
```
COS738_Assignment/
│
├── Project1_EC_Cipher/
│   ├── ec_cipher.py
│   ├── screenshots/
│   └── README.md
│
├── Project2_GUI/
│   ├── ec_password_gui.py
│   ├── Project1/
│   │   └── ec_password_generator.py
│   ├── gui_screenshots/
│   └── README.md
│
├── Project3_Java_Translation/
│   ├── ECPasswordGUI.java
│   ├── ECPasswordGenerator.java
│   ├── screenshots/
│   └── README.md
│
└── Overview_README.md  ← (this file)
```

---

## 🧠 Theoretical Background
The system leverages **Evolutionary Computing (EC)** and **Symbolic Regression** to simulate random number generation using real noise data (e.g. Random.org).  
By using **TuringBot**, a nonlinear mathematical function is evolved, which serves as a cipher generator.  

This cipher replaces the standard random number generator in password generation, ensuring that:
- The passwords are **deterministic**, **strong**, and **unique** to the user.  
- The encryption logic is **AI-assisted** and adaptable.

The research foundation is detailed in:
> Blackledge et al. (2025), *Application of Evolutionary Computing for Generating Encryption Algorithms with AI-based Code Generation*, IntechOpen.

---

## ⚙️ Project Descriptions

### **Project 1 – EC Cipher Generation**
**Goal:**  
Develop your own nonlinear cipher function using **TuringBot**.

**Steps:**
1. Load 50 data points of real noise (e.g. from Random.org).  
2. Use **TuringBot** to evolve a formula approximating this dataset.  
3. Replace the existing `ec_formula(row)` in the provided Python code with your evolved function.  
4. Test and validate the function by ensuring it outputs a random-like cipher stream.

**Deliverables:**
- Screenshot of your TuringBot run and evolved formula.
- Updated Python script with your own `ec_formula(row)`.
- Short write-up describing the observed randomness and iteration behavior.

---

### **Project 2 – GUI for Strong Password Generator**
**Goal:**  
Create a **Tkinter GUI** that allows the user to:
- Input a **memorable (weak)** password.
- Choose the **desired length** of the strong password.
- Output and display the resulting **strong password**, also written to file.

**Features:**
- GUI components: Input fields, output box, generate button, save-to-file option.
- Uses the EC cipher function from Project 1.
- Demonstrates deterministic yet strong password generation.

**Files:**
- `ec_password_gui.py`
- `ec_password_generator.py`

**Deliverables:**
- Screenshots of the running GUI.
- Source code files.
- Short documentation describing GUI components and how it works.

---

### **Project 3 – Java Translation**
**Goal:**  
Translate the Python-based EC Password Generator (from Project 2) into **Java**, using **Swing** for the GUI.

**Files:**
- `ECPasswordGenerator.java` — core logic equivalent of `ec_password_generator.py`
- `ECPasswordGUI.java` — GUI implementation using Swing components

**Key Classes:**
```java
// ECPasswordGenerator.java
public class ECPasswordGenerator {
    public static double ecFormula(double row) { ... }
    public static String generatePassword(String memorablePassword, int length) { ... }
}

// ECPasswordGUI.java
public class ECPasswordGUI extends JFrame {
    private JTextField passwordField;
    private JTextField lengthField;
    private JTextArea outputArea;
    // Event-driven generation using ECPasswordGenerator
}
```

**Deliverables:**
- Screenshots of the Java GUI.
- Source code of both Java classes.
- Short write-up comparing performance and usability between Python (Tkinter) and Java (Swing).

---

## 🧪 Testing and Validation
- **Input:** Memorable password and desired password length.
- **Output:** Strong password and `.txt` file with stored results.
- **Validation:** Ensure the strong password is consistent for the same inputs.
- **Cross-language check:** The Java output should match the Python version for the same inputs.

---

## 🧰 Technologies Used
| Component | Technology | Purpose |
|------------|-------------|----------|
| Cipher Generation | Python (TuringBot Output) | EC-based cipher formula |
| GUI Prototype | Python (Tkinter) | GUI for password generation |
| Translation | Java (Swing) | Cross-language code validation |
| Data Source | Random.org | Real random noise |
| AI Support | ChatGPT / Copilot | Code generation & translation |

---

## 🎥 Demonstration
You are required to include an `.mp4` demonstration showing:
- GUI functionality (input → output).
- Explanation of how the EC-based generator works.
- Comparison of the Python and Java GUIs.

---

## 📑 Marking Scheme
| Component | Weight | Description |
|------------|---------|-------------|
| Functionality | 50% | Code runs correctly and produces valid outputs. |
| Code Clarity | 25% | Readability, structure, and use of comments. |
| Documentation | 25% | Short written explanations and screenshots. |

---

## 🧾 References
1. Blackledge, J.M., Kingstone, R., & Midgley, B. (2025). *Application of Evolutionary Computing for Generating Encryption Algorithms using AI-based Code Generation.* IntechOpen.  
2. Walker, D. (2025). *How Do Hackers Get Your Passwords?* ITPro.  
3. NIST Cryptographic Algorithm Validation Program (2025).  
4. TuringBot.com and Random.org APIs.  

---

## 🧠 Summary
This project demonstrates how **AI** and **Evolutionary Computing** can be leveraged to create **personalized, strong password systems** that are secure, deterministic, and replicable.  
By progressing from **Python cipher generation → GUI implementation → Java translation**, the project highlights the fusion of AI-driven code generation with cryptographic logic.

---

## 📂 Submission Checklist
✅ Project 1, 2, and 3 subfolders with respective code and screenshots  
✅ Overview README.md (this file)  
✅ `.mp4` demonstration video  
✅ TuringBot screenshot (Project 1)  
✅ GUI screenshots (Python + Java)  
✅ All code properly documented  

---

**Author:**  
Jaydin Morrison  
**Student No.:** 4260354  
**Course:** COS738 – Cyber Security  
**Institution:** University of the Western Cape  
**Year:** 2025
