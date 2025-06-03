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
    try:
        title = request.args.get("title", default="", type=str)
        if not title:
            return jsonify({"error": "Title parameter is required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title = ?", (title,))

        posts = cursor.fetchall()
        content_list = [post["content"] for post in posts]

        if not content_list:
            return jsonify({"error": "Post not found"}), 404

        return jsonify(content_list)

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
