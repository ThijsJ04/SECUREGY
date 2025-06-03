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
    title = request.args.get(
        "title"
    )  # Assuming this is the URL parameter '/get_post?title=your_title'

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    conn.close()  # Close the connection

    return "{content}".format(**result) if result else "No post found with that title."
