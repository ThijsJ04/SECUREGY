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
    title = request.args.get("title", "")

    if not title:
        return {"status": "error", "message": "Title parameter is required"}

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT content FROM posts WHERE title = %s"
    cursor.execute(query, (title,))

    post = cursor.fetchone()

    conn.close()

    if not post:
        return {"status": "error", "message": "Post not found"}

    return {
        "status": "success",
        "data": {"content": post["content"]},
        "message": "Post retrieved successfully",
    }
