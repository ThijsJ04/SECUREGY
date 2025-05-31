import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    try:
        cursor.execute('SELECT content FROM posts WHERE title = ?', (title,))
        result = cursor.fetchone()
        if result:
            return {'content': str(result['content'])}, 200
        else:
            return {'message': 'Post not found'}, 404
    except sqlite3.Error as e:
        db_connection.rollback()
        return {'error': str(e)}, 500
    finally:
        db_connection.close()