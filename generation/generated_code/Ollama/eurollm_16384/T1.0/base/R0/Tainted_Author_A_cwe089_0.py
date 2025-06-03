import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    title = request.args.get("title")
    # Establish a connection to your SQLite database using the get_db_connection function
    with get_db_connection() as conn:
        cur = conn.cursor()
        query = "SELECT * FROM posts WHERE title=?"
        cur.execute(
            query, (title,)
        )  # Pass the query and the parameters to the execute method
        row = cur.fetchone()  # Fetch one row from the query result
    if not row:  # Check if a post was found
        return "Post not found", 404
    content = str(row["content"])  # Convert the "content" column's value to a string
    return content, 200  # Return the post's content with an HTTP status code of 200 OK
