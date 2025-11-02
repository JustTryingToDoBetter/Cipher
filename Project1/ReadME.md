# Project 1 – Unique Cipher Generation using TuringBot
**Module:** COS738 Cybersecurity (Blackledge 2025)  
**Student:** Jaydin Morrison (4260354)  
**Weighting:** 20% of final mark  

---

## 🚀 Overview
This project generates a **unique nonlinear cipher function** using **TuringBot**.  
The cipher is integrated into a Python-based strong password generator (`ec_password_generator.py`) as part of an Evolutionary Computed (EC) system.

Goal:
- Create an AI-evolved formula using symbolic regression.
- Integrate it into a deterministic password generator.
- Produce complex, high-entropy passwords from simple memorable inputs.

---

## ⚙️ Configuration Summary
**Dataset:**  
- 50 random floats between 0 and 1  
- Columns: `x` (0–1 progression) and `y` (random noise)  

**TuringBot Configuration:**  
- Maximum formula size: 100  
- Maximum history size: 20  
- Bound search mode: Deactivated  
- Normalize dataset: ✅ Enabled  
- CPU threads: 8  
- Function set: `+ - * / sin cos tan exp log tanh cosh atanh`  
- Error metric: RMSE  

**Search Duration:** ≈ 1 minute  
**Total formulas tested:** ~6.7 million  

---

## 🧠 Generated Cipher Function
**Final evolved formula:**
```python
f(x) = 0.245247 - 0.00355652 * (
    tan(x + 0.997621) -
    (2.50253 * tan(x + x + 0.990735) + 41.4887 -
    (tan(1.99855 + atanh(x) - 0.996519) + tan(x + 0.928126)/(-2.46095)) *
    (0.986526 + (atanh(x) - 0.918575) * (x - 1.04439 + 2.59159 * x)) +
    x * (x + 1) + tan(1.42159 + x) -
    tan((-12.2847) * x + (-9.10391) * x))
)
```

**Performance:**
```
RMSE = 0.240814
```

This formula demonstrates nonlinearity and sufficient entropy for secure password generation.

---

## 🧩 Integration
In `ec_password_generator.py`, replace the placeholder `ec_formula(row_value)` with the generated function:

```python
def ec_formula(row_value: float) -> float:
    return 0.245247 - 0.00355652 * (
        math.tan(row_value + 0.997621) -
        (2.50253 * math.tan(row_value + row_value + 0.990735) + 41.4887 -
        (math.tan(1.99855 + math.atanh(row_value) - 0.996519) +
         math.tan(row_value + 0.928126)/(-2.46095)) *
        (0.986526 + (math.atanh(row_value) - 0.918575) *
        (row_value - 1.04439 + 2.59159 * row_value)) +
        row_value * (row_value + 1) + math.tan(1.42159 + row_value) -
        math.tan((-12.2847) * row_value + (-9.10391) * row_value))
    )
```

---

## 🧪 Testing
Run:
```bash
python ec_password_generator.py --memorable "maskiplayground" --length 20
```
Output example:
```
^X1zU+uY$p(]n8O0xL!
```

---

## 📸 Evidence
Screenshot of final TuringBot session:  
`turing_results.png` (shows formula, RMSE = 0.240814, and graph output)

---

## 🧾 Deliverables
```
Project1/
├── ec_password_generator.py
├── turingbot_input.csv
├── turingbot_results.png
└── README.md
```

---

## 🧑‍💻 Author
**Jaydin Morrison**  
COS738 Cybersecurity Student (Eduvos)  
2025
