import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    title = request.args.get("title")

    if not title:
        return "Title parameter is required", 400

    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))
    row = cursor.fetchone()

    if not row:
        return "Post not found", 404
    else:
        content = row["content"]
        cursor.close()
        conn.close()
        return content
