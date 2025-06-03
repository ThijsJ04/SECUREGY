import sqlite3
from flask import Flask, request

app = Flask(__name__)


# Define a decorator to handle exceptions
def safe_execute(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            print("SQLite error:", e)
            return "Error fetching data"

    return wrapper


# Define a decorator to handle exceptions for the database connection
def safe_connect(func):
    def wrapper(*args, **kwargs):
        try:
            conn = func()
            return conn
        except sqlite3.Error as e:
            print("Database error:", e)
            return None

    return wrapper


# Define a decorator to handle exceptions for the database query
def safe_query(func):
    def wrapper(*args, **kwargs):
        try:
            with conn:
                return func(*args, **kwargs)
        except sqlite3.Error as e:
            print("Database error:", e)
            return None

    return wrapper


# Connect to the database
@safe_connect
def get_db_connection():
    conn = sqlite3.connect("./database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
@safe_query
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title")
    if not title:
        return "Error: Title is required"

    query = """SELECT * FROM posts WHERE title = ?"""
    rows = cur.execute(query, (title,))
    post_data = rows.fetchone() or None

    if not post_data:
        return "Post not found"

    return str(post_data)
