from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'securekey123' 



def get_db():
return sqlite3.connect('users.db')



def create_table():
db = get_db()
db.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT
)
""")
db.commit()


create_table()


@app.route('/signup', methods=['GET', 'POST'])
def signup():
if request.method == 'POST':
username = request.form['username']
password = request.form['password']


if not username or not password:
return "Fields cannot be empty"


hashed_password = generate_password_hash(password)


try:
db = get_db()
db.execute("INSERT INTO users (username, password) VALUES (?, ?)",
(username, hashed_password))
db.commit()
return redirect('/login')
except:
return "Username already exists"


return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
username = request.form['username']
password = request.form['password']


db = get_db()
user = db.execute("SELECT * FROM users WHERE username = ?",
(username,)).fetchone()


if user and check_password_hash(user[2], password):
session['user'] = username
return redirect('/dashboard')
else:
return "Invalid credentials"


return render_template('login.html')

@app.route('/dashboard')
def dashboard():
if 'user' in session:
return render_template('dashboard.html', user=session['user'])
return redirect('/login')


# ---------------- LOGOUT ----------------
app.run(debug=True)
