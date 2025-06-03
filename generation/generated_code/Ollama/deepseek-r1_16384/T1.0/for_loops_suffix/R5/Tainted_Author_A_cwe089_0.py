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
    title = request.args.get("title", "")
    if not title:
        return "Title parameter is required"

    conn = get_db_connection()
    with conn:
        cursor = conn.execute("SELECT content FROM posts WHERE title = ?", (title,))
        posts = cursor.fetchall()

    content_list = [post["content"] for post in posts]
    return jsonify(content_list)
