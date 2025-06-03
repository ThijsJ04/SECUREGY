import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    try:
        # Get the title from the request's parameters
        title = request.args.get("title")

        if not title or not isinstance(title, str):
            return "Error: Title must be a string", 400

        # Query the database for the post with the given title
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
        result = cursor.fetchone()

        if not result:
            return f'No post found with title "{title}"', 404

        # Return the post's content as a JSON response
        data = {"content": result[1], "author": result[2]}

    except sqlite3.Error as e:
        return f"Database error: {e}", 500

    finally:
        if conn:
            conn.close()

    return jsonify(data), 200
