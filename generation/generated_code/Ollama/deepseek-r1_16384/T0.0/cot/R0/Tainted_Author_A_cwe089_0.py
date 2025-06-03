import sqlite3
from flask import Flask, request, jsonify

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
    title = request.args.get("title", "")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    cursor = conn.execute(
        "SELECT content FROM posts WHERE title LIKE ?", (f"%{title}%",)
    )
    posts = [dict(row) for row in cursor.fetchall()]

    if not posts:
        conn.close()
        return jsonify({"error": "Post not found"}), 404

    content = "\n".join([post["content"] for post in posts])
    conn.close()
    return jsonify({"content": content}), 200
