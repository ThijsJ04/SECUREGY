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
    conn = get_db_connection()
    try:
        query = "SELECT * FROM posts WHERE title = ?"
        params = (
            request.args.get("title"),
        )  # Get the title from the request parameters
        result = conn.execute(query, params).fetchone()
        return str(result[1]) if result else "Post not found"
    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        conn.close()
