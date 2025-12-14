-->Security Features Included
Input validation
Password hashing (no plain text passwords)
Protection against SQL Injection
Basic session management
Protection against XSS (using template escaping)

-->Project Structure
secure_app/
│── app.py
│── users.db
└── templates/
  │── signup.html
  │── login.html
  │── dashboard.html

-->How Security Is Achieved (Simple Explanation)
Threat	          Protection Used
SQL               Injection	Prepared statements (?)
Password Theft	  Password hashing
XSS	              Flask auto‑escaping
Session Hijacking	Flask sessions
Weak Inputs	Basic input validation

-->How to Run
pip install flask werkzeug
python app.py
