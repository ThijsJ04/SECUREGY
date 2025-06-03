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
    title = request.args.get("title")  # Get the title from the query string

    if not title:
        return "Title is required", 400

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM posts WHERE title=?"
    cursor.execute(sql, (title,))  # Execute the SQL query with the provided title
    row = cursor.fetchone()  # Fetch the row from the database

    if not row:
        return f"No post found for '{title}'", 404

    content = row[1]  # Get the content of the post
    conn.close()  # Close the connection to the database

    return content, 200
