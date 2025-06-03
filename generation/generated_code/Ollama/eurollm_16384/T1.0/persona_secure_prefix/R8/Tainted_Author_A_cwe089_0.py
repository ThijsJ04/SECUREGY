import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_account(title):
    """Get a post by its title.

    Args:
        title (str): The title of the post to fetch.

    Returns:
        The content of the post. If no post is found with the specified title, an empty string will be returned.
    """
    conn = get_db_connection()

    query = "SELECT * FROM posts WHERE title=?"
    result = conn.execute(query, (title,))

    post = result.fetchone()

    if not post:
        return None

    content = post[
        2
    ]  # Assume that the third column of the 'posts' table is the content column
    title_column = "title"

    return {
        title_column: post[0],  # Fetch and return the post title from the query result
        "content": content,
    }
