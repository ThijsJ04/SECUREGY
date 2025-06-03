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
    title = request.args.get("title")

    if not title:
        return "Title not specified"

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM posts WHERE title = ?", (title,))
        row = cursor.fetchone()
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        conn.close()

    if row is None:
        return "Post not found"
    else:
        return str(row["content"])
