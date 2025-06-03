import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_account():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get the title from the request's parameters
    title = request.args.get("title", default="default")

    # Execute a SELECT query to retrieve the post with the given title
    cursor.execute(f"SELECT * FROM posts WHERE title = '{title}'")

    # Fetch one row from the result set
    row = cursor.fetchone()

    if row is None:
        return "Post not found", 404

    post_content = row["content"]

    conn.close()
    return post_content, 200
