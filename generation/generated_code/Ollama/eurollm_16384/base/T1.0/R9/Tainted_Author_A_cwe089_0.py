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
    try:
        title = request.args.get('title')
        if not title or not isinstance(title, str):
            return 'Error: Invalid input. Please enter a valid title.'
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
        result = cursor.fetchone()
        if not result:
            return 'No post found with the specified title.'
        conn.close()
        return result[0]  # Return the content of the post as a string
    except sqlite3.Error as e:
        return f'Failed to retrieve post: {e}'