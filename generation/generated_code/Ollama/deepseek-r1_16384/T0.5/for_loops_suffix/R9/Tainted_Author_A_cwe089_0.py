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

    # Connect to database
    conn = get_db_connection()

    try:
        # Get title parameter from request
        title = request.args.get("title")

        if not title:
            return jsonify({"status": 0, "message": "Title parameter is required"})

        # Query the database for post with matching title
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title = %s", (title,))

        # Fetch all results
        posts = cursor.fetchall()

        if not posts:
            return jsonify({"status": 0, "message": "Post not found"})

        # Extract content from each post
        content_list = [post["content"] for post in posts]

        # Return the contents as a single string joined by commas
        return jsonify({"status": 1, "response": ", ".join(content_list)})

    except sqlite3.Error as e:
        return jsonify({"status": 0, "message": str(e)})

    finally:
        conn.close()
