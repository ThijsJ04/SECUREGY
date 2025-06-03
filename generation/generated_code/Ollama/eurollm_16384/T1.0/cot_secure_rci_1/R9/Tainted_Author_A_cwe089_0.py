import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """Get the post with a specific title."""
    title = request.args.get("title")  # Get the title from the query string

    conn = get_db_connection()  # Connect to your database

    query = "SELECT * FROM posts WHERE title=?"  # SQL query to select the post with a specific title

    result = conn.execute(
        query, (title,)
    )  # Execute the SQL query and fetch the results
    post_content = (
        result.fetchone()[1] if result.rowcount > 0 else None
    )  # Fetch the post content from the database

    conn.close()  # Close the database connection
    return post_content, 200  # Return the post content and HTTP OK status code
