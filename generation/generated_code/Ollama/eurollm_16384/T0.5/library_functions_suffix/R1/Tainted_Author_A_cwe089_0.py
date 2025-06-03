import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")  # Connect to the database file
    return conn


@app.route("/get_post", methods=["GET"])
def get_account(title):
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()  # Get database connection

    query = f"SELECT * FROM posts WHERE title='{title}'"
    cursor = conn.cursor()
    cursor.execute(query)
    record = cursor.fetchone()

    if record:  # If a post with the given title exists
        return str(record[1])  # Return the content of the post
    else:
        return "Post not found", 404


@app.route("/get_post", methods=["POST"])
def get_account_post():
    conn = get_db_connection()

    title = request.form["title"]  # Get the title from the form data
    query = f"INSERT INTO posts (title) VALUES ('{title}')"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return "Post created successfully", 201
