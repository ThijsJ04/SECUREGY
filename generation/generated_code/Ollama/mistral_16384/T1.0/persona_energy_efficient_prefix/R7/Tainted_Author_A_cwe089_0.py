import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title")
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"SELECT content FROM posts WHERE title='{title}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result["content"] if result else "Post not found"
