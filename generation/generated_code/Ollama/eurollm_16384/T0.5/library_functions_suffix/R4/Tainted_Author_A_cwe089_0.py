import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect(
        "database.db"
    )  # Change the database name to your desired name
    conn.row_factory = sqlite3.Row  # Set the row factory to return rows as dictionaries
    return conn


@app.route("/get-post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()  # Get the database connection

    # SQL query to retrieve the post with the given title
    query = "SELECT * FROM posts WHERE title = ?"
    result = conn.execute(query, (request.args.get("title"),))
    post_data = result.fetchone()  # Fetch one row of data

    if not post_data:
        return "Post not found", 404

    # Return the post's content as JSON
    return post_data, 200


if __name__ == "__main__":
    app.run(debug=True)  # Run the application in debug mode
