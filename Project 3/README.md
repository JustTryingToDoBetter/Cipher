# Project 3 – Translation to C# (Windows Forms)

## 📘 Overview
This project forms **Part 3** of the COS738 Cyber Security Assignment under J M Blackledge (2025).  
The task is to **translate** the Python‐based GUI application (developed in Project 2) into another programming language using an AI-assisted workflow.  

The chosen language is **C# /.NET 6 (Windows Forms)**, which provides a modern, object-oriented framework for building secure and responsive GUI applications.

---

## 🧠 Concept Summary
The application generates a **strong password** from a **memorable (weak) password** using an **Evolutionary-Computed Cipher (EC Cipher)** function derived from the TuringBot symbolic-regression process discussed in *Pre-publication.pdf*.

- The EC Cipher function is a nonlinear iterative equation that simulates a pseudo-random number stream.
- The stream is transformed to a uniform distribution.
- Each element of the uniform stream is mapped to printable ASCII characters to form a reproducible strong password.
- The generated password is displayed in the GUI and written to a local text file for reference.

---

## 🧩 Features
✅ GUI with input fields for:
  - Memorable (weak) password  
  - Desired strong password length  
✅ Strong password output field  
✅ File output to `ec_strong_password.txt`  
✅ Error handling for invalid inputs  
✅ 1:1 logic parity with Python version from Project 2  

---

## ⚙️ Implementation Details
**Language & Framework:**  
- C# /.NET 6 (LTS)  
- Windows Forms App  

**Key Components:**
| Component | Description |
|------------|--------------|
| `EcFormula(row)` | Evolutionary-Computed nonlinear cipher function |
| `GenerateRandomNumberStream(seed, length)` | Iteratively produces cipher values |
| `TransformToUniform(array)` | Normalises output to a uniform distribution |
| `GenerateEcStrongPassword(memorable, length)` | Generates reproducible strong password |
| GUI | Built using Windows Forms controls (`TextBox`, `NumericUpDown`, `Button`, `Label`) |

**Dependencies:**  
No external packages required beyond standard .NET libraries.

---

## 🧑‍💻 How to Run
1. **Open in Visual Studio 2022 (or later)**  
   - File → New → Project → *Windows Forms App (.NET 6)*  
2. **Replace auto-generated files**  
   - Copy the provided `ECPasswordGenerator.cs` and `MainForm.Designer.cs` contents.  
3. **Build and Run (F5)**  
4. **Usage:**  
   - Enter a *memorable password* (e.g. `maskiplay23`)  
   - Choose desired *length* (e.g. `20`)  
   - Click **Generate Password**  
   - View result on-screen and in `ec_strong_password.txt`

---

## 🧾 Example Output
```
Memorable password: maskiplay23
Strong password: Ff<o;g]e@A:\~%WVCb[
File saved as: ec_strong_password.txt
```

---

## 🧱 File Structure
```
Project3/
 ├── ECPasswordGenerator.cs
 ├── MainForm.Designer.cs
 ├── README.md
 └── ec_strong_password.txt  (runtime output)
```

---

## 🎓 Learning Outcome
- Demonstrated AI-assisted **code translation** from Python → C#.  
- Applied **Evolutionary Computing concepts** to password generation.  
- Showcased **secure GUI development** in C# with deterministic output parity.  
- Illustrated modern software-engineering practice integrating cryptographic theory with AI-based tooling.

---

## 🧑‍🏫 Reference
Blackledge J M., Kingstone R., & Midgley B. (2025).  
*Application of Evolutionary Computing for Generating Encryption Algorithms with AI-based Code Generation.*  
In *Coding Theory: Advances in Communications Engineering and Information Security*, IntechOpen.

---

**Author:** Jaydin Morrison  
**Module:** COS738 Cyber Security  
**Institution:** University of the Western Cape  
**Date:** October – November 2025  
