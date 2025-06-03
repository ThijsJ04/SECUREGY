import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("Database/database.db")
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    title = request.args.get(
        "title", default="Default Title"
    )  # Get the title from the URL parameter if not provided
    try:
        with get_db_connection() as conn:
            cur = conn.cursor()
            query = f"""SELECT * FROM posts WHERE title = '{title}'"""  # Build a SQL query to find the post with the given title
            cur.execute(query)
            result = cur.fetchone()  # Fetch and return one row of results
        return (
            str(result[1]) if result else "No posts found"
        )  # Return the content of the post or a message indicating no matches
    except sqlite3.Error as e:
        print(e)
        return f"An error occurred: {e}"  # Return an error message in case of database issues
