import sqlite3
from flask import Flask, request, jsonify
import logging

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
        # Connect to database
        conn = get_db_connection()

        # Extract title from request parameters
        title = request.args.get("title")

        if not title:
            return jsonify({"error": "Title parameter is required"}), 400

        # Query the database for posts matching the title
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))

        # Fetch all results
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"message": "Post not found"}), 404

        # Collect content from each row
        posts_content = [{"content": row["content"]} for row in rows]

        return jsonify(posts_content)

    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return jsonify({"error": "Internal database error"}), 500
    finally:
        if "conn" in locals():
            conn.close()


if __name__ == "__main__":
    app.run(debug=True)
