# WAST QUESTIONNAIRE FOR PERU (ONLINE VERSION)

## 📝 Project Description

This project is an interactive, lightweight **static web application** implementing the **Woman Abuse Screening Tool (WAST)**.  
It was developed to provide a **fast, reliable, and modern** tool to assess intimate partner violence risk, especially adapted to the **Peruvian context**.

Many existing NGO platforms in Peru fail due to accessibility or technical issues — some crash before completing the survey, while others only offer outdated PDFs.  
This project aims to deliver a **robust, accessible, and always-available digital tool** for self-assessment and early detection, hosted directly on **GitHub Pages**.

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

Built as a serverless static web application using **HTML5, Vanilla JavaScript (ES6+), and Bootstrap 5.3.3**.  
The entire application runs 100% client-side inside the user's browser, eliminating backend server dependencies, lowering latency, and maximizing user privacy.

### Main File

| File | Description |
|------|--------------|
| **index.html** | Self-contained single-page application holding the UI layout, Bootstrap styling, survey dataset (`QUESTIONS`, `RISK_LEVELS`), and evaluation logic. |

---

## ⚙️ Key Design Decisions

### 1. Controlled Survey Flow
- Application state is managed dynamically in memory via JavaScript.
- Validates user input step-by-step, preventing premature access to evaluation results or skipping unanswered questions.

### 2. Maximum Privacy and Anonymity
- **100% Client-Side Processing**: No user responses are ever sent to, or stored on, remote servers or databases.
- State is kept only in temporary browser memory and is completely wiped clean upon closing or refreshing the browser tab.

### 3. High Availability and Zero Maintenance
- Hosted on **GitHub Pages** for maximum uptime, high loading speed, and zero server management overhead.
- Fully responsive design using Bootstrap 5.3.3, optimized for mobile phones and desktop displays.

---

## 🎯 Conclusion

This project provides a **clinically validated, accessible, and context-aware screening tool for Peru**, leveraging static web architecture to deliver an instant, secure, and private experience for users.

---

## 🚀 How to Run the Project Locally

Since this project has no backend dependencies, running it locally is simple:

### Option 1: Direct File Access
Double-click `index.html` or drag the file directly into any web browser.

### Option 2: Local HTTP Server (Python)
Run a local web server from your project terminal:

```bash
python3 -m http.server 8000