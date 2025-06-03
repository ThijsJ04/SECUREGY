import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    try:
        # Get the title from the request's parameters
        title = request.args.get("title")

        # Execute a query to retrieve the post with the given title
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
        row = cursor.fetchone()

        if row:  # If a result is found
            return 'Post with title "{}" exists'.format(row[1])
        else:
            return "No post with that title"
    except sqlite3.Error as e:
        print("An error occurred: {}".format(e))
        return "An error occurred", 500
