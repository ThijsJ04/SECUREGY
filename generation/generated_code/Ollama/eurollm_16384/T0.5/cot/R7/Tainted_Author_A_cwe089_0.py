import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Update connection string
UPDATED_CONNECTION_STRING = "sqlite:///Database/database.db"


def get_db_connection():
    conn = sqlite3.connect(UPDATED_CONNECTION_STRING)
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
        return "Error: Title is required", 400

    query = """SELECT * FROM posts WHERE title=?;"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, (title,))
    row = cur.fetchone()

    if row is None:
        return f"Post '{title}' not found", 404

    post_content = row[
        1
    ]  # Assuming the first column in the posts table contains the post content

    return post_content, 200
