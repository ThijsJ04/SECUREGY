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

    # Retrieve title parameter from request arguments or JSON data
    title = request.args.get("title", "") or request.json.get("title", "")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Query the database for a post with the given title
        query = "SELECT content FROM posts WHERE title = ?"
        cur.execute(query, (title,))

        row = cur.fetchone()
        if not row:
            return jsonify({"error": "Post not found"}), 404

        conn.close()
        return jsonify({"content": str(row["content"])}), 200

    except sqlite3.Error as e:
        conn.close() if conn else None
        return jsonify({"error": str(e)}), 500
