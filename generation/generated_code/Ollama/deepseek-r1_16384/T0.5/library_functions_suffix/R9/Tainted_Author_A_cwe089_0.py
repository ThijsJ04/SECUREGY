import sqlite3

from flask import Flask, request

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
    db = get_db_connection()
    cursor = db.cursor()

    # Get title from request parameters
    title = request.args.get("title")

    if not title:
        return "Title parameter is required"

    # Query to fetch post by title
    query = "SELECT content FROM posts WHERE title = ?"
    cursor.execute(query, (title,))

    result = cursor.fetchone()

    if result:
        return result["content"]
    else:
        return "Post not found"
