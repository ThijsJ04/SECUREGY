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
    title = request.args.get("title")  # Get the title from the GET request
    if not title:
        return "Title is required", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    sql_query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(
        sql_query, (title,)
    )  # Execute the SQL query with the title as a parameter
    row = cursor.fetchone()  # Fetch the first row of the result

    if not row:
        return "Post not found", 404

    post_content = row[1]  # Get the content from the result
    conn.close()  # Close the database connection

    return post_content, 200
