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
    title = request.args.get("title")  # Get the value of 'title' parameter if it exists
    if not title:
        return "Title is required", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """SELECT * FROM posts WHERE title = ?"""
    cursor.execute(sql, (title,))  # Execute the query with the provided title
    result = cursor.fetchone()  # Fetch one row from the result set

    if not result:
        return "Post not found", 404

    post_content = result[1]  # Get the content of the post
    conn.close()  # Close the database connection

    return post_content, 200
