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

    # Get title parameter from request
    title = request.args.get("title")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Query to fetch post by title
    query = "SELECT content FROM posts WHERE title = ?"
    cursor.execute(query, (title,))

    row = cursor.fetchone()

    conn.close()

    if not row:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({"content": row["content"]}), 200
