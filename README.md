# 🔒 Secure My Portfolio Kit

A lightweight Python tool that scans your website (or portfolio) for missing **security headers** and generates a simple **HTML report**.  
Perfect for developers who want to **learn about web security** and ensure their personal sites are safer.

---

## 🚀 Features
- Checks for common security headers:
  - **Strict-Transport-Security (HSTS)**
  - **Content-Security-Policy (CSP)**
  - **Referrer-Policy**
  - **Permissions-Policy**
  - **X-Frame-Options**
  - **X-Content-Type-Options**
- Grades your site’s security posture (A–F).
- Outputs results to both **terminal** and a **styled HTML report**.
- Supports scanning **one site** or **multiple sites in batch**.
- Beginner-friendly project to understand **basic cybersecurity concepts**.

---

## 🛠️ Requirements
- Python **3.10+**
- `pip` to install dependencies
- Internet connection

---

## 📦 Installation
```bash
# 1. Clone this repository
git clone https://github.com/AnasAyub-08/secure-my-portfolio-kit
cd secure-my-portfolio-kit

# 2. (Optional) Create and activate a virtual environment
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the script
python scanner.py https://example.com