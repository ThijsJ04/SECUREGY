import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    conn = get_db_connection()
    # Retrieve the required parameters from the request
    title = request.args.get("title")  # Replace 'title' with the correct parameter name

    # Query the database to find the post with the specified title
    posts = conn.execute("SELECT * FROM posts WHERE title = ?", (title,))

    # Fetch one row of data from the query result
    post = next(posts) if posts else None

    if post is not None:
        # Return the post content as a JSON response
        post_content = f"{{ 'title': {post['title']}, 'body': {post['body']} }}"
        return post_content, 200

    else:
        # Return an error message if no results are found
        return "Post not found", 404
