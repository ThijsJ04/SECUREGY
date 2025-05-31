import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post', methods=['GET'])
def get_account():
    """Get the post with a specific title."""

    # Get the title from the request's parameters
    title = request.args.get('title')

    # Query the database for the post with the given title
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
    row = cursor.fetchone()  # Fetch one row from the query result
    conn.close()  # Close the database connection

    if not row:
        return "Post not found", 404

    # Return the post's content as JSON
    return {"content": row[1], "is_blog": True}, 200