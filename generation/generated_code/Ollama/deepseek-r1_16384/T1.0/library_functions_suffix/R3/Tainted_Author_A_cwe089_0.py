import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title", "")
    if not title:
        return jsonify({"error": "Title is required"}), 400

    conn = get_db_connection()
    try:
        cursor = conn.execute("SELECT content FROM posts WHERE title = ?", (title,))
        post = cursor.fetchone()

        if post is None:
            return jsonify({"error": "Post not found"}), 404

        return jsonify({"content": post["content"]})
    finally:
        conn.close()
