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
        return "Title parameter is required", 400

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title = ? LIMIT 1", (title,))
        row = cursor.fetchone()

        if row:
            return str(row["content"])
        else:
            return "Post not found", 404
    finally:
        conn.close()


# To test the endpoint, you can use a tool like curl or a browser.
# Example using curl:
# curl "http://localhost:5000/get_post?title=your_desired_title"
