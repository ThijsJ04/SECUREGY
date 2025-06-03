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

    # Get post content based on title (assuming you have a function or method to fetch posts by title)
    post_content = my_post_fetcher(
        title
    )  # Replace 'my_post_fetcher' with your actual implementation

    conn.close()
    return post_content
