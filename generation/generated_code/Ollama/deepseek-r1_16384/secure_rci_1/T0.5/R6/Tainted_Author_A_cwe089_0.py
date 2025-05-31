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
    if 'title' not in request.args:
        return "Error: No title provided"

    title = request.args['title']
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM posts WHERE title LIKE ?"
    cursor.execute(query, (title,))

    posts = cursor.fetchall()
    conn.close()

    if not posts:
        return "No post found with the given title."

    # Assuming each post has a 'content' field
    contents = [post['content'] for post in posts]
    return f"Post content(s): {contents}"