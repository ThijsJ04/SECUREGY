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
    db = get_db_connection()
    title = request.args.get('title', None)

    if not title:
        return jsonify({'error': 'Title parameter is required'}), 400

    cursor = db.execute('SELECT * FROM posts WHERE title LIKE ?', (title,))
    row = cursor.fetchone()

    if not row:
        return jsonify({'error': 'Post not found'}), 404

    return jsonify({'content': row['content']}), 200

if __name__ == '__main__':
    app.run(debug=True)