import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    title = request.args.get('title', '').strip()
    if not title:
        return jsonify({'error': 'Title is required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT content FROM posts WHERE title = ? LIMIT 1"
        cursor.execute(query, (title,))

        row = cursor.fetchone()
        if row:
            return jsonify({'content': str(row['content'])}), 200
        else:
            return jsonify({'error': 'Post not found'}), 404
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'Internal server error'}), 500
    finally:
        cursor.close()
        conn.close()