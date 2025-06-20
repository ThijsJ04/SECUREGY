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
    title = request.args.get("title")
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE title=?"
    cursor.execute(sql, (title,))
    row = cursor.fetchone()
    if row:
        return str(row[1])  # Return the post's content as a string
    else:
        return "Post not found"
