import sqlite3
from flask import Flask, request
import json

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
    db = get_db_connection()
    cursor = db.cursor()

    # Get title parameter from request
    title = request.args.get('title')

    if not title:
        return "Title parameter is required", 400

    # Query to fetch post by title
    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))

    result = cursor.fetchall()

    if len(result) == 0:
        db.close()
        return json.dumps({'error': 'Post not found'}), 404

    post = dict(result[0])
    db.close()
    return json.dumps(post), 200