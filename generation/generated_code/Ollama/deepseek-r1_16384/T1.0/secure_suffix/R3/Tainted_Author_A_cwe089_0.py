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

    title = request.args.get("title")
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT content FROM posts WHERE title = ?"
        cursor.execute(query, (title,))

        row = cursor.fetchone()

        if not row:
            return jsonify({"error": "Post not found"}), 404

        return jsonify({"content": row["content"]}), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
