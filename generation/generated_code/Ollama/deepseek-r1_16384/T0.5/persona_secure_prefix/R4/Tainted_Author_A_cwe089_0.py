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
    # Get the title parameter from the request
    title = request.args.get("title")

    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Query the database for a post with the given title
        cursor.execute("SELECT id, title, content FROM posts WHERE title = ?", (title,))
        row = cursor.fetchone()

        if not row:
            return jsonify({"error": "Post not found"}), 404

        # Return the post's content as JSON
        return jsonify({"content": str(row["content"])}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
