import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Get the title from the query string

    query = "SELECT * FROM posts WHERE title=?"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (title,))
    row = cursor.fetchone()  # Fetch the first row of results

    if row:
        post_content = row[1]  # The second column is the content
        return f"Post with title '{title}': {post_content}"
    else:
        return "No post found with that title."