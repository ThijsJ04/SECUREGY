import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_post(title):
    conn = get_db_connection()
    query = f"SELECT * FROM posts WHERE title='{title}';"
    rows = conn.execute(query).fetchall()
    post = rows[0] if len(rows) > 0 else None
    conn.close()
    return post
