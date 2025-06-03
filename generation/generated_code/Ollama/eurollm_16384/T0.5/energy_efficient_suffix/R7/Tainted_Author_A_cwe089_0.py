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
        # Get the title parameter from the request
        title = request.args.get("title")
        if not title:
            return "Title is required", 400

        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM posts WHERE title=?"
            cursor.execute(query, (title,))
            result = cursor.fetchone()

        if not result:
            return "Post not found", 404

        return str(result[1]) + "<br>" + str(result[2]) + "<br>" + str(
            result[3]
        ) + "<br>" + str(result[4]), 200
    except Exception as e:
        print(e)
        return "An error occurred", 500
