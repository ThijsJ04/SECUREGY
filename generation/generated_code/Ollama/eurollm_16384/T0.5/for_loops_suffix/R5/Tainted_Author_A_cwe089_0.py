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

    # SQL query to select the post with the given title
    query = f"SELECT * FROM posts WHERE title='{title}'"

    try:
        result = conn.execute(query)
        post = result.fetchone()

        if not post:  # If no results are found, return an empty response
            return {"error": "Post not found"}

        # Return the post content as a JSON-formatted string
        return f"{post['title']}: {post['content']}"
    except sqlite3.Error as e:
        print(f"SQL error: {e}")
    finally:
        conn.close()
