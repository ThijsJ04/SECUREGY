from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_account(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post = cursor.fetchone()
    conn.close()
    if post:
        return jsonify({'content': post['content']})
    else:
        return '', 404

@app.route('/get_post')
def get_account_from_request():
    title = request.args.get('title')
    if not title:
        return '', 400
    return get_account(title)