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
    title = request.args.get("title", "")

    if not title:
        return "Title parameter is required"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE title = ?", (title,))

    row = cursor.fetchone()

    conn.close()

    if row:
        return str(row["content"])
    else:
        return f'Post with title "{title}" not found'


# The complete code is provided above, including the helper function and route handler.
