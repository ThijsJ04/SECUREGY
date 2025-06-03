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
    title = request.args.get("title", "").strip()
    cursor = conn.cursor()

    query = "SELECT content FROM posts WHERE title = ?"
    cursor.execute(query, (title,))
    post = cursor.fetchone()

    if not post:
        return "Post not found", 404
    else:
        return post["content"]


if __name__ == "__main__":
    app.run(debug=True)
