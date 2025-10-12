# WAST QUESTIONNAIRE FOR PERU (ONLINE VERSION)

## 📝 Project Description

This project is an interactive **Flask web application** implementing the **Woman Abuse Screening Tool (WAST)**.  
It was developed to provide a **fast, reliable, and modern** tool to assess intimate partner violence risk, especially adapted to the **Peruvian context**.

Many existing NGO platforms in Peru fail due to accessibility or technical issues — some crash before completing the survey, while others only offer outdated PDFs.  
This project aims to deliver a **robust, accessible, and always-available digital tool** for self-assessment and early detection.

---

## 🔬 Clinical Basis and Methodology

The questionnaire is based on the **Woman Abuse Screening Tool (WAST)**, a recognized international clinical standard.

### ✅ Why Choose WAST Over Other Tools

| Feature | WAST (Woman Abuse Screening Tool) |
|----------|-----------------------------------|
| **Validity** | High. Validated in multiple countries, including Spanish versions. |
| **Reliability** | Cronbach’s Alpha > 0.80 (Highly acceptable). |
| **Strength** | Evaluates both physical and emotional abuse, offering comprehensive screening. |
| **Limitation** | Slightly longer (8 questions), but accuracy compensates for length. |

Based on:  
> Fogarty, C. T., & Brown, J. B. (2002). *Screening for abuse in Spanish-speaking women*. The Journal of the American Board of Family Practice, 15(2), 101–111.

---

## 💻 Architecture and Technical Design

Built using **Flask (Python)** and deployed with **Gunicorn** for production environments.  
All questionnaire logic and scoring are handled in-memory using session variables, ensuring privacy and eliminating the need for persistent databases.

### Main Files

| File | Description |
|------|--------------|
| **app.py** | Main application logic: routes, session handling, and score calculation. |
| **data.py** | Contains static data: `QUESTIONS`, `RISK_LEVELS`, and `SAFETY_PLAN`. |
| **requirements.txt** | Dependencies list (Flask, Gunicorn, matplotlib). |

---

## ⚙️ Key Design Decisions

### 1. Anti-Skipping Protection

A common problem in online surveys is URL manipulation to skip questions — this is critical in risk evaluations.

- **Implementation:** In `/question/<int:num>`, sequential validation ensures no question can be skipped.  
  If a user tries to jump from Q3 to Q8, they’re redirected to the first unanswered question.

- **`/results` Route Locked:** Accessible only after all questions are completed.

---

### 2. Privacy and Anonymity

No personal data or login system is required.  
All sessions are temporary, ensuring complete anonymity and privacy.  
This design choice prioritizes safety and accessibility for all users.

---

### 3. Accessibility and Reliability

- Fully compatible with **mobile and desktop browsers**.  
- Lightweight and fast thanks to **Flask + Gunicorn** setup.  
- No external dependencies such as databases or authentication systems.

---

## 🎯 Conclusion

This project provides a **clinically validated, accessible, and context-aware screening tool for Peru**, addressing existing technical gaps and empowering women to assess risk safely and privately.

---

## 🚀 How to Run the Project

To run the project locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Start the Flask app with Gunicorn
gunicorn app:app
