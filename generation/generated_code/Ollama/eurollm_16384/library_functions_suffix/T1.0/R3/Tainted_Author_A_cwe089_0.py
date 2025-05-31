import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect('database.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    """Returns the post with a specific title."""
    # Get the title from the request parameters.
    title = request.args.get('title')
    if not title:
        return 'Error: Title is required', 400

    # Execute the query to retrieve the post data.
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE title=?", (title,))
    row = cursor.fetchone()
    conn.close()

    # Return the post's content as a string.
    if row:
        return str(row[1]) + '<br>' + str(row[2])
    else:
        return 'Post not found', 404