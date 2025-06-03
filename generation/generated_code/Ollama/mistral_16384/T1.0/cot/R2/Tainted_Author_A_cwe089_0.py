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
    query = "SELECT content FROM Post WHERE title=?"
    cursor.execute(query, (title,))
    post = cursor.fetchone()
    if not post:
        return "Post not found", 404
    else:
        conn.close()
        return post["content"]
