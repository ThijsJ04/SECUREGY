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
    conn = get_db_connection()
    cursor = conn.cursor()

    title = request.args.get("title", default=None)

    if not title:
        return "Title parameter is required."

    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))
    result = cursor.fetchall()

    if not result:
        cursor.close()
        conn.close()
        return f"No post found with title: {title}"

    post = result[0]
    content = post["content"]
    cursor.close()
    conn.close()
    return content
