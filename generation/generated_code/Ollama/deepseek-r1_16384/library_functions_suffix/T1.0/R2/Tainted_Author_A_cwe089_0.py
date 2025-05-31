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
    title = request.args.get('title')

    if not title:
        return jsonify({'error': 'Title parameter is required'}), 400

    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            query = "SELECT * FROM posts WHERE title = :title"
            cursor.execute(query, {'title': title})

            if not cursor.row_factory:
                conn.close()
                return jsonify({'error': 'Database error'}), 500

            row = cursor.fetchone()
            if not row or cursor.rowcount < 1:
                conn.close()
                return jsonify({'message': 'Post not found'}), 404

            content = str(row['content'])
            conn.close()
            return jsonify({'content': content}), 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500