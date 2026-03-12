# db_table_app.py
from flask import Flask, render_template_string
import sqlite3
import os

DB = "data.db"
app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    qty INTEGER NOT NULL,
                    price REAL NOT NULL
                )""")
    # insert sample if empty
    c.execute("SELECT COUNT(*) FROM items")
    if c.fetchone()[0] == 0:
        sample = [
            ("Apple", 10, 0.5),
            ("Banana", 20, 0.3),
            ("Orange", 15, 0.6),
        ]
        c.executemany("INSERT INTO items (name, qty, price) VALUES (?, ?, ?)", sample)
    conn.commit()
    conn.close()

init_db()

HTML = """
<!doctype html>
<title>Items Table</title>
<h2>Items (from SQLite)</h2>
<table border=1 cellpadding=6>
  <tr><th>ID</th><th>Name</th><th>Quantity</th><th>Price</th></tr>
  {% for row in rows %}
    <tr>
      <td>{{ row[0] }}</td>
      <td>{{ row[1] }}</td>
      <td>{{ row[2] }}</td>
      <td>{{ "%.2f"|format(row[3]) }}</td>
    </tr>
  {% endfor %}
</table>
"""

@app.route("/")
def show_table():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, name, qty, price FROM items ORDER BY id")
    rows = c.fetchall()
    conn.close()
    return render_template_string(HTML, rows=rows)

if __name__ == "__main__":
    app.run(debug=True, port=5003)
