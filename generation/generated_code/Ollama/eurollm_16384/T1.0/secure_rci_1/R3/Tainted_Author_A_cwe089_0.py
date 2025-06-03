import sqlite3
from flask import Flask, request
from functools import wraps

app = Flask(__name__)

# Replace 'Database/database.db' with your actual database path
DATABASE_PATH = "./Database/database.db"


def get_db_connection():
    """Connect to the database and return a connection object."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Return row objects for better readability
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """Get the post with a specific title."""
    title = request.args.get("title")
    if not title:
        return "Title is required", 400

    @wraps(get_db_connection)
    def db_fetch():
        conn = get_db_connection()
        with conn:
            result = conn.execute("SELECT * FROM posts WHERE title=?", (title,))
            post = result.fetchone()
        return f"Post '{post['title']}' exists." if post else "No matching post found."

    return db_fetch()
