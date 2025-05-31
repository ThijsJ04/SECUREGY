import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    try:
        # Connect to database and retrieve the post by title
        conn = get_db_connection()
        query = "SELECT * FROM posts WHERE title = ?"
        cur = conn.cursor()
        cur.execute(query, (request.args.get('title'),))
        row = cur.fetchone()
        if row is None:
            return {'error': 'Post not found'}
        post_data = {}
        post_data['id'] = row[0]
        post_data['content'] = row[1]
    except sqlite3.Error as e:
        # Handle any database errors that may occur
        return {'error': 'Failed to retrieve post'}

    finally:
        # Close the database connection if it was opened
        conn.close()
    return {'data': post_data}