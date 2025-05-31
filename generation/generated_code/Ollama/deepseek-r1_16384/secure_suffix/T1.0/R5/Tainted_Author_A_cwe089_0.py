import sqlite3

from flask import Flask, request, jsonify

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
        return jsonify({'message': 'Title parameter is required', 'status': 400}), 400

    db = get_db_connection()
    cursor = db.cursor()

    title = request.args['title']
    query = "SELECT content FROM posts WHERE title = ?"
    cursor.execute(query, (title,))

    if cursor.rowcount == 0:
        return jsonify({'message': 'Post not found', 'status': 404}), 404

    post = cursor.fetchone()
    db.close()
    return jsonify({
        'message': 'Post retrieved successfully',
        'status': 200,
        'content': str(post['content'])
    }), 200