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
    conn = get_db_connection()
    try:
        sql = "SELECT * FROM posts WHERE title = ?"
        result = conn.execute(sql, (request.args['title'],))
        row = result.fetchone()
        if row:
            return str(row[1])  # Return the content of the post
        else:
            return "Post not found", 404
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()