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
        conn = get_db_connection()
        cursor = conn.cursor()

        title = request.args.get("title", "")
        if not title:
            return jsonify({"error": "Title parameter is required"}), 400

        # Assuming posts table has columns: id, title, content
        cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))
        post = cursor.fetchone()

        if not post:
            return jsonify({"error": f"Post with title {title} not found"}), 404

        content = str(post["content"])
        conn.close()
        return jsonify({"content": content}), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if "conn" in locals():
            conn.close()
