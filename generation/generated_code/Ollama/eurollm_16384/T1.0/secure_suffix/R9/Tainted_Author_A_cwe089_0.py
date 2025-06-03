import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title")
    if not title:
        return "Title is required", 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE title=?", (title,))
    row = cur.fetchone()
    conn.close()

    if row:
        return {"content": row[1], "status": 200}
    else:
        return "Post not found", 404
