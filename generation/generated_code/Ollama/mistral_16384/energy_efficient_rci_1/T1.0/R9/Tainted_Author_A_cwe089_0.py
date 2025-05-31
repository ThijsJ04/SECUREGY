from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post_content = cursor.fetchone()['content'] if cursor.rowcount > 0 else None
    conn.close()
    return jsonify({'post_content': post_content})