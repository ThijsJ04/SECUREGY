import sqlite3
from flask import Flask, request
from functools import wraps

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_post():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()

    title = request.args.get('title')

    query = "SELECT * FROM posts WHERE title=?;"
    cur = conn.cursor()
    cur.execute(query, (title,))
    row = cur.fetchone()

    if row:
        post_id, content = row
        return f"<h1>{content}</h1>", 200
    else:
        return "<p>No post found with the given title.</p>", 404