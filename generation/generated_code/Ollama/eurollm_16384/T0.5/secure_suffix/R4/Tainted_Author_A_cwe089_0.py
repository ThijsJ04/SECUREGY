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
    conn = get_db_connection()
    title = request.args.get("title")

    query = "SELECT * FROM posts WHERE title=?"
    cursor = conn.cursor()
    cursor.execute(query, (title,))
    row = cursor.fetchone()

    if row:
        return str(row)  # Return the post's content as JSON
    else:
        return "Post not found"  # Return a message if no post is found
