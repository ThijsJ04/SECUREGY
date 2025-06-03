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
    try:
        title = request.args.get("title")
        if not title or title == "all":
            return get_all_posts()
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
            row = cursor.fetchone()
            conn.close()
            return row[1] if row else "No post found"
    except sqlite3.Error as e:
        return str(e)
