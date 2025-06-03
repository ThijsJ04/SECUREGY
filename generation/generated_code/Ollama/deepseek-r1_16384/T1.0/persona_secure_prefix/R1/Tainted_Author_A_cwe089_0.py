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
    if "title" not in request.args:
        return "Error: No title provided", 400
    conn = get_db_connection()
    try:
        title = request.args["title"]
        cursor = conn.execute(
            "SELECT content FROM posts WHERE title = ? LIMIT 1", (title,)
        )
        result = cursor.fetchone()
        if result is None:
            return "Error: Post not found", 404
        return result["content"]
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)
