import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account(title):
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM posts WHERE title=?"
            cursor.execute(query, (title,))
            post = cursor.fetchone()
            if post:
                return f'<h1>{post["title"]}</h1><p>{post["content"]}</p>'
        return 'Post not found', 404
    except sqlite3.Error as e:
        print(f'SQLite error: {e}')
        return f'An error occurred: {str(e)}', 500