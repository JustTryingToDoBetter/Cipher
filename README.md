
# 🔐 Cipher: Evolutionary Computed Strong Password Generator  
**COS738 Cybersecurity Project (2025)**  
Developed by: *Jaydin Morrison*  
Supervisor: *Professor J.M. Blackledge*  
Institution: *University of the Western Cape*  
Date: *November 2025*  

---

## 📘 Overview

**Cipher** is a complete software project developed for the **COS738 Cybersecurity Specialist Seminar** module.  
It demonstrates how **Evolutionary Computing (EC)** and **AI-based code generation** can be applied to design, test, and deploy a **strong password generator** that evolves cryptographic ciphers.

The project consists of **three deliverables**:
1. Generation of a **unique cipher** using **TuringBot**
2. Design and implementation of a **Python GUI**
3. **Translation to C#** using AI-assisted development (ChatGPT)

The system transforms a **weak, memorable password** into a **strong, reproducible password**, combining *cryptographic theory*, *AI automation*, and *evolutionary computation*.

---

## 📂 Project Structure

```
Cipher/
│
├── Project1/                # Evolutionary Computed Cipher (EC) Generation
│   ├── ec_formula.py
│   ├── turingbot_input.csv
│   ├── results_screenshot.png
│   └── README_Project1.md
│
├── Project2/                # GUI Implementation in Python
│   ├── gui_main.py
│   ├── assets/
│   ├── screenshots/
│   └── README_Project2.md
│
├── Project3/                # Translated C# Version
│   ├── CipherGUI.csproj
│   ├── MainWindow.xaml
│   ├── MainWindow.xaml.cs
│   └── README_Project3.md
│
└── README.md                # Main documentation file
```

---

## 🧬 Project 1 — Evolutionary Cipher Generation

### 🎯 Objective
Generate a **unique cipher function** using **TuringBot** based on *real random noise* from **Random.org**, applying symbolic regression to model nonlinear randomness.

### 🧠 Concept
TuringBot evolves mathematical formulas through symbolic regression to simulate random number streams.  
This allows the creation of **bespoke encryption functions** that can regenerate identical ciphers from the same key input.

### ⚙️ Example Output Function
```python
def ec_formula(row):
    return 0.432357 + (-0.498752 * math.cos(
        0.594808 * (-4.10993 * math.cosh(row) -
        (0.590558 + math.atanh(math.cos(
        math.tan(math.cos(row / (-0.00153462))) + row * row))))))
```

### 🧩 Process Summary
1. Export 50 random numbers from **Random.org**
2. Load dataset into **TuringBot**
3. Evolve the formula using trigonometric, exponential, and hyperbolic functions
4. Integrate the output formula into the Python program
5. Test uniformity using statistical rank transformation

### 🧪 Deliverables
- Custom EC formula
- Screenshot of TuringBot result
- Test run output in Python console

---

## 🧩 Project 2 — GUI Design (Python)

### 🎯 Objective
Create a **Graphical User Interface** that enables:
- Input of a weak (memorable) password  
- Specification of output string length  
- Display and file export of a **strong deterministic password**

### 🛠️ Implementation
Framework: `tkinter`  
Backend: Custom EC cipher module (`ec_formula`)  
Language: Python 3.11  

### 💡 Features
- Deterministic password generation (same input → same output)  
- Local file logging of generated password  
- AI-generated code refined manually for readability and structure  

---

## 💻 Project 3 — Language Translation (Python → C#)

### 🎯 Objective
Recreate the entire GUI-based strong password generator in **C#** using **AI-based translation**.

### ⚙️ Example C# Translation
```csharp
public static double EcFormula(double row)
{
    return 0.432357 - 0.498752 * Math.Cos(
        0.594808 * (-4.10993 * Math.Cosh(row) -
        (0.590558 + Math.Atanh(Math.Cos(
        Math.Tan(Math.Cos(row / (-0.00153462))) + row * row)))));
}
```

### 🧩 Testing
- Verified deterministic consistency with Python version  
- Adjusted `Math.Atanh()` and exception handling for .NET  
- Confirmed GUI parity using WPF  

---

## 🧠 Theory Summary

### Evolutionary Computing
Simulates natural selection to evolve cipher functions for cryptographic randomness.

### Symbolic Regression
Uses mathematical evolution to simulate true random noise functions.

### AI Integration
ChatGPT automates GUI generation, translation, and debugging.

---

## 🧩 Appendix

### Appendix A — AI Prompts Used
| Task | Prompt |
|------|---------|
| Generate Cipher Function | “Use symbolic regression output from TuringBot to generate a Python function simulating a nonlinear cipher.” |
| GUI Design | “Create a tkinter GUI for the strong password generator using the cipher function and file output.” |
| C# Translation | “Translate the Python GUI and cipher generation program to C# using WPF.” |

### Appendix B — Screenshot Captions
1. *TuringBot nonlinear evolution process*  
2. *Python GUI interface displaying generated password*  
3. *C# translated application showing equivalent output*  

---

## 🧾 License

**Creative Commons Attribution 4.0 License (CC BY 4.0)**  
You may use, adapt, and distribute this material with proper citation.

---

## 🏁 Conclusion

The **Cipher** project demonstrates the use of **AI-driven code generation** and **evolutionary computing** in practical cybersecurity applications.  
By evolving nonlinear cipher functions via TuringBot and deploying them in Python and C#, this project proves that:
> “AI-assisted cryptography empowers individuals to design their own secure, dynamic encryption methods.”
