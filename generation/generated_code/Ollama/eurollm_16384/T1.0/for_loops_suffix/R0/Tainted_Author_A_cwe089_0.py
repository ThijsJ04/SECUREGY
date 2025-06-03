import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_post(title):
    conn = get_db_connection()
    query = f"SELECT content FROM posts WHERE title='{title}'"
    post = conn.execute(query).fetchone()
    if post:
        return {"content": post["content"]}
    else:
        return {"message": "Post not found"}
