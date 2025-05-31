import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()
    try:
        # Get the title from the URL path
        title = request.args.get('title')

        # Execute a SELECT query to fetch the post with the given title
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM posts WHERE title='{title}'")

        # Fetch one row from the result
        row = cursor.fetchone()

        if row:
            return f'Post with title "{title}": {row[1]}', 200
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

@app.route('/create_post')
def create_post():
    '''
    Create a new post with title and content.
    '''
    conn = get_db_connection()
    try:
        title = request.args.get('title')
        content = request.args.get('content')

        # Execute an INSERT query to add the new post
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO posts (title, content) VALUES ('{title}', '{content}')")
        conn.commit()
        return f'Post created: {title} - {content}', 201
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()