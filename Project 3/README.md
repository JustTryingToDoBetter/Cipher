# Project 3 – Translation to Java  
### COS738 Cyber Security Assignment (2025)  
**Student:** Jaydin Morrison  
**Module:** COS738 Cyber Security  
**Lecturer:** Dr J M Blackledge  
**Assignment Component:** Translation of Python GUI to Java (Language Conversion)

---

## 📘 Overview

This project forms **Project 3** of the COS738 specialist seminar series:  
> “Developing a GUI for a Strong Password Generator using an Evolutionary Computed Cipher and AI-based Code Generation.”

Following the completion of the Python implementation (Projects 1 & 2), the codebase was translated into **Java**, implementing the same Evolutionary Computing (EC) formula to generate strong, deterministic passwords from user-defined memorable strings.  

This Java version reproduces the Python behaviour exactly, while using the **JavaFX** framework for the graphical interface.

---

## 🧩 Structure

```
Project3/
│
├── ECPasswordGenerator.java   ←  Core EC cipher logic and password generator
├── ECPasswordGUI.java         ←  JavaFX GUI wrapper for user interaction
└── README.md                  ←  Documentation file (this file)
```

### 1️⃣ `ECPasswordGenerator.java`
Implements the full deterministic password-generation pipeline:

- Converts a **memorable password** into a reproducible floating-point seed via SHA-256 hashing.  
- Iterates the **Evolutionary Computed (EC) cipher** (`ecFormula`) to produce a pseudo-random numeric stream.  
- Applies a **rank-based uniform transformation** to remove statistical bias.  
- Maps the uniform stream to printable ASCII characters (`!`–`~`) to yield the strong password.  

### 2️⃣ `ECPasswordGUI.java`
Implements the GUI using **JavaFX**:

| Element | Description |
|----------|-------------|
| **Memorable Password Input** | Text field for user’s weak but memorable key |
| **Desired Length Input** | Numeric field specifying output string length |
| **Generate Button** | Runs the EC cipher pipeline and displays output |
| **Output Box** | Displays generated strong password |
| **Save Button** | Saves password to `ec_strong_password.txt` |
| **Status Label** | Displays operation messages (Ready, Success, Error) |

The GUI design follows the aesthetic of the Python Tkinter version (dark theme, green highlight, modern fonts).

---

## ⚙️ Execution Instructions

### 🧠 Requirements
- Java 17 or newer  
- JavaFX SDK (17 or later)

### 🧰 Compilation & Run Commands
Example (Windows PowerShell):

```bash
javac --module-path "C:\javafx\lib" --add-modules javafx.controls *.java
java  --module-path "C:\javafx\lib" --add-modules javafx.controls ECPasswordGUI
```

Example (macOS / Linux):

```bash
javac --module-path /opt/javafx/lib --add-modules javafx.controls *.java
java  --module-path /opt/javafx/lib --add-modules javafx.controls ECPasswordGUI
```

---

## 🔐 Algorithm Summary

| Step | Description |
|------|-------------|
| 1 | **Input** a memorable password and desired output length |
| 2 | Convert password → float seed (SHA-256 hash) |
| 3 | Iterate the **EC formula** (TuringBot-evolved cipher) |
| 4 | Transform → uniform distribution using rank data |
| 5 | Map → printable ASCII range (33–126) |
| 6 | Display and optionally save the result |

### EC Formula (From TuringBot)
```java
val = 0.245247
      - 0.00355652 * tan(x + 0.997621)
      - (2.50253 * tan(x + x + 0.990735))
      + 41.4887
      - (tan(1.99855 + atanh(x)) - 0.996519)
      + (tan(x + 0.928126) / -2.46095)
        * (0.986526 + (atanh(x) - 0.918575))
        * (x - 1.04439 + 2.59159 * x)
      + x * (x + 1)
      + tan(1.42159 + x)
      - tan((-12.2847) * x + (-9.10391) * x);
```
(Safe math wrappers prevent division-by-zero or infinite results.)

---

## 💻 Screenshots (to include)

- GUI main window showing input fields and generated password.  
- Example output file (`ec_strong_password.txt`) containing saved password.  
- Console build output from `javac` / `java` commands (for validation).

---

## 🧠 Reflection

| Aspect | Observation |
|---------|--------------|
| **Language Translation** | Demonstrated AI-assisted conversion from Python (Tkinter + NumPy) to Java (JavaFX + core libraries). |
| **Functional Equivalence** | Verified that both versions produce identical passwords for the same inputs. |
| **Performance** | Java iteration loop performs faster for long lengths (>10 000 chars). |
| **Security Considerations** | Password saved locally with overwrite mode; recommended to use secure storage and deletion policies. |

---

## 📦 Deliverables

- ✅ Source files (`ECPasswordGenerator.java`, `ECPasswordGUI.java`)  
- ✅ Executable demo (`.mp4` screen recording showing JavaFX app running)  
- ✅ This `README.md` explanation  
- ✅ Screenshot evidence (folder `/screenshots`)  

---

## 📚 References

1. J M Blackledge et al., *Application of Evolutionary Computing for Generating Encryption Algorithms using AI-based Code Generation*, IntechOpen, 2025.  
2. COS738 Cyber Security Module Guide, University of the Western Cape (2025).  
3. OpenAI ChatGPT (GPT-5), for code translation assistance (Python → Java).  
4. Oracle JavaFX Documentation, 2025.

---

**End of README**
