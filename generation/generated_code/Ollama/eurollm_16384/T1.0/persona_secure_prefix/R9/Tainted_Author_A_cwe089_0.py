import sqlite3
from flask import Flask, request

app = Flask(__name__)


# Establish a connection to the database
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
    title = request.args.get("title")
    query = "SELECT * FROM posts WHERE title=?"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        query, (title,)
    )  # (?, ?) is a placeholder for the parameterized query
    row = cursor.fetchone()
    if row:
        post = row["content"]
        return f"Post found with title '{title}' and content '{post}'."
    else:
        return "No post found with the specified title."
