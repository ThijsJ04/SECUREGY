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
    title = request.args.get('title')
    if not title:
        return 'Error: Title is required', 400

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM posts WHERE title=?"
    cursor.execute(sql, (title,))
    result = cursor.fetchone()

    if result is None:
        return 'Post not found', 404

    post_content = result[1]  # Assuming the post content is stored in the second column of the table

    conn.close()
    return post_content, 200