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
    '''
    try:
        title = request.args.get('title')
        if not title or title == 'None':
            return "Title is required", 400

        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM posts WHERE title='{title}'"
        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            return {'content': row[1]}
        else:
            return "Post not found", 404
    except sqlite3.Error as e:
        print(e)
        return f"An error occurred: {e}", 500
    finally:
        if conn:
            conn.close()