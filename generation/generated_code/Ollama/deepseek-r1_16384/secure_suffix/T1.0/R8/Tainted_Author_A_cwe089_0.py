import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    title = request.args.get('title', '')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE title = ?", (title,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is not None:
        return row['content']
    else:
        return ''

# Ensure the database table exists with appropriate schema
# Sample SQL setup for posts table (run once outside application):
# CREATE TABLE IF NOT EXISTS posts (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT UNIQUE,
#     content TEXT
# );