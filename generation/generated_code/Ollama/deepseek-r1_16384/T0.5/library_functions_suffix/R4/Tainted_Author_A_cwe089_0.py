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
        db = get_db_connection()
        cursor = db.cursor()

        # Get title parameter from request
        title = request.args.get("title")
        if not title:
            return jsonify({"error": "Title is required"}), 400

        # Query the database for the post with given title
        query = "SELECT content FROM posts WHERE title = ?"
        cursor.execute(query, (title,))

        # Fetch the result
        result = cursor.fetchone()
        if not result:
            return jsonify({"error": "Post not found"}), 404

        # Return the post content
        return jsonify({"content": str(result["content"])}), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
