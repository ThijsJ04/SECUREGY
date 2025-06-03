import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    title = request.args.get("title")
    conn = get_db_connection()
    query = "SELECT * FROM posts WHERE title = ?"
    result = conn.execute(query, (title,))
    post = result.fetchone()
    if not post:
        return "Post not found", 404
    else:
        content = post[1]  # Assuming the first column is the post's text
        return content
