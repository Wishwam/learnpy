from flask import Flask, request, redirect, url_for, session, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "secret123")

DB = "auth.db"

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- HTML PAGES ----------------

REGISTER_HTML = """
<h2>Register</h2>
<form method="post">
Username:<br>
<input name="username" required><br><br>

Password:<br>
<input type="password" name="password" required><br><br>

<button type="submit">Register</button>
</form>

<p style="color:red;">{{message}}</p>

<p>Already registered? <a href="/login">Login</a></p>
"""

LOGIN_HTML = """
<h2>Login</h2>
<form method="post">
Username:<br>
<input name="username" required><br><br>

Password:<br>
<input type="password" name="password" required><br><br>

<button type="submit">Login</button>
</form>

<p style="color:red;">{{message}}</p>

<p>Don't have account? <a href="/register">Register</a></p>
"""

PROFILE_HTML = """
<h2>Welcome {{username}}</h2>
<p>You are successfully logged in.</p>

<a href="/logout">Logout</a>
"""

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return redirect(url_for("login"))

# -------- REGISTER --------
@app.route("/register", methods=["GET", "POST"])
def register():

    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        password_hash = generate_password_hash(password)

        try:
            conn = sqlite3.connect(DB)
            c = conn.cursor()

            c.execute(
                "INSERT INTO users(username,password_hash) VALUES(?,?)",
                (username, password_hash)
            )

            conn.commit()
            conn.close()

            return redirect(url_for("login"))

        except:
            message = "Username already exists"

    return render_template_string(REGISTER_HTML, message=message)

# -------- LOGIN --------
@app.route("/login", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()

        c.execute(
            "SELECT id,password_hash FROM users WHERE username=?",
            (username,)
        )

        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[1], password):

            session["user_id"] = user[0]
            session["username"] = username

            return redirect(url_for("profile"))

        else:
            message = "Invalid username or password"

    return render_template_string(LOGIN_HTML, message=message)

# -------- PROFILE --------
@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template_string(
        PROFILE_HTML,
        username=session["username"]
    )

# -------- LOGOUT --------
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))

# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True, port=5001)

