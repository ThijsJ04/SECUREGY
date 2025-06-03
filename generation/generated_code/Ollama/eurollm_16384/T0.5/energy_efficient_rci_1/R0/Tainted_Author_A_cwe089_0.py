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
    conn = get_db_connection()
    try:
        title = request.args.get("title")
        if title is None or len(title) == 0:
            return "Title required", 400
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
        row = cursor.fetchone()
        if row is None:
            return "Post not found", 404
        return str(row[1]), 200
    except sqlite3.Error as e:
        print("SQLite error: {}".format(e))
    finally:
        conn.close()
