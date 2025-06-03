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
    title = request.args.get("title")
    if not title:
        return "Title parameter is required", 400

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT content FROM posts WHERE title = ?"
        cursor.execute(query, (title,))
        post = cursor.fetchone()

        if post:
            return f"Content: {post['content']}"
        else:
            return f"No post found with title: {title}", 404
    finally:
        cursor.close()
        conn.close()
