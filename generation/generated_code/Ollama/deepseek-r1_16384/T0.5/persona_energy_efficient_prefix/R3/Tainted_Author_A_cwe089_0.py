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
    import json

    db = get_db_connection()
    cursor = db.cursor()

    title = request.args.get("title")

    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))
    row = cursor.fetchone()

    if not row:
        db.close()
        return jsonify({"error": "Post not found"}), 404

    content = str(row["content"])
    db.close()
    return jsonify({"content": content}), 200
