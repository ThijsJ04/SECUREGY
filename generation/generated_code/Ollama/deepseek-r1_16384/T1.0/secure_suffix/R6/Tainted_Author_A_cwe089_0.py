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
    cursor = conn.cursor()

    title = request.args.get("title", "")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))

    row = cursor.fetchone()

    if row:
        post_content = dict(row)
        conn.close()
        return jsonify(post_content["content"]), 200
    else:
        conn.close()
        return jsonify({"message": "Post not found"}), 200
