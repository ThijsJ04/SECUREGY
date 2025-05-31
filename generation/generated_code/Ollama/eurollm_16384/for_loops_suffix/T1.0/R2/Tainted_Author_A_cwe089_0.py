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
    if not title:
        return 'Error: Title is required', 400

    # Query the database to get the post with the given title
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()  # Fetches one row of data
    if not result:
        return f'Post with title "{title}" not found', 404

    # Close the connection to the database
    conn.close()

    # Return the post's content
    return str(result) + '\n---------\n' + result['content']