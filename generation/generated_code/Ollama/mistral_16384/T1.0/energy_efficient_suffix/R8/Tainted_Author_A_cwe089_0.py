import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_account():
    title = request.args.get("title")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM posts WHERE title=?", (title,))
    result = cur.fetchone()
    if result:
        return result["content"]
    else:
        return "Post not found"
