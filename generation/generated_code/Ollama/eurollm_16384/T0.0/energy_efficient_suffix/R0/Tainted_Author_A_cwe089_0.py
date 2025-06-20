import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account(title):
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM posts WHERE title=?"
    cursor.execute(query, (title,))
    row = cursor.fetchone()
    if row:
        return str(row[1])  # Return the post's content as a string
    else:
        return "Post not found", 404


@app.route("/get_post", methods=["POST"])
def get_account():
    title = request.form["title"]
    query = "INSERT INTO posts (title) VALUES (?)"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (title,))
    conn.commit()
    return f"Post {title} created successfully", 201
