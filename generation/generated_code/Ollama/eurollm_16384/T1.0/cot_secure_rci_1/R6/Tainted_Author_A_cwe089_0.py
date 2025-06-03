import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")  # specify the database file
    conn.row_factory = sqlite3.Row  # format result rows as dictionaries
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """Get the post with a specific title."""
    params = request.args  # access GET parameters from the request URL
    title = params.get("title")  # extract the 'title' parameter value

    conn = get_db_connection()

    query = "SELECT * FROM posts WHERE title=?"
    rows = conn.execute(query, (title,))  # execute SQL query with the title parameter

    post = rows.fetchone()  # fetch one row from the result
    if post:
        return str(post[1])  # return the post content as a string
    else:
        return "Post not found"


if __name__ == "__main__":
    app.run(debug=True)
