import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    try:
        title = request.args.get("title")
        query = "SELECT * FROM posts WHERE title = ?"
        cur = conn.cursor()
        cur.execute(query, (title,))
        result = cur.fetchone()
    except sqlite3.OperationalError:
        return "Could not find post with the given title."
    finally:
        conn.close()
    if result:
        return f"<p>Post Title: {result['title']}</p><p>Post Content: {result['content']}</p>"
    else:
        return "No post found with the given title."
