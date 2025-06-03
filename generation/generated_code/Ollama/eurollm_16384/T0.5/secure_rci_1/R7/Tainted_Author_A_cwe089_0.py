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
        if not title:
            return "Title is required", 400

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL query to select the post with a specific title
        query = "SELECT * FROM posts WHERE title=?;"
        cursor.execute(query, (title,))

        # Fetch one row from the result
        row = cursor.fetchone()

        if not row:
            return "Post not found", 404

        # Return the post's content as a JSON object
        data = {"title": row[1], "content": row[2]}

    except sqlite3.Error as e:
        return "Database error", 500
    finally:
        if conn:
            conn.close()

    return jsonify(data)
