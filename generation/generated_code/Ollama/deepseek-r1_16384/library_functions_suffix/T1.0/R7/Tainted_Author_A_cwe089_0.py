import sqlite3
from flask import Flask, request, jsonify
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post')
def get_account():
    title = request.args.get('title', '')
    if not title:
        return jsonify({'error': 'Title is required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title = ?", (title,))
        posts = cursor.fetchall()

        contents = []
        for post in posts:
            content = str(post['content'])
            contents.append(content)

        return jsonify(contents), 200
    except Exception as e:
        print(f"Error fetching post: {e}")
        return jsonify({'error': 'Failed to fetch post'}), 500
    finally:
        if conn:
            conn.close()