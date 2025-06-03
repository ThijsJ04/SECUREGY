import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    # Get the post title from the request parameters
    title = request.args.get(
        "title"
    )  # Assuming the title is provided in the query string as a key-value pair (e.g., "/get_post?title=Post Title")

    if not title:
        return "Title is required", 400

    conn = get_db_connection()

    # Execute the query to fetch the post content based on the specified title
    query = "SELECT * FROM posts WHERE title=?"
    result = conn.execute(query, (title,))
    post = result.fetchone()  # Fetch one row from the result set

    if not post:
        return "Post not found", 404

    # Return the post's content as a response
    return {"post": post[1]}, 200
