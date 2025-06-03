import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
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

    # SQL query to fetch the post with the given title
    query = "SELECT * FROM posts WHERE title=?"

    try:
        cursor.execute(query, (title,))  # Pass the title as a tuple
        row = cursor.fetchone()  # Fetch one row of result
    except sqlite3.OperationalError:
        return "Post not found", 404

    conn.close()  # Close the database connection

    return str(row) if row else "", 200  # Return the post's content as a string
