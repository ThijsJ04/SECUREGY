import sqlite3
from flask import Flask, request, jsonify
from datetime import datetime

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
        return jsonify({'error': 'Title parameter is required'}), 400

    title = request.args['title']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            SELECT p.*, u.username AS author
            FROM posts p
            JOIN users u ON p.user_id = u.id
            WHERE p.title = ?
        """
        cursor.execute(query, (title,))

        posts = []
        for row in cursor.fetchall():
            post_data = dict(row)
            post_data['created_at'] = post_data['created_at'].isoformat() if post_data['created_at'] else None
            post_data['updated_at'] = post_data['updated_at'].isoformat() if post_data['updated_at'] else None
            posts.append(post_data)

        conn.close()

        if not posts:
            return jsonify({'error': 'Post not found'}), 404

        return jsonify(posts)
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({'error': 'Internal server error'}), 500