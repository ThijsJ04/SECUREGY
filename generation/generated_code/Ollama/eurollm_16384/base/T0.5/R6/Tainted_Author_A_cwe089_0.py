import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account(title):
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'SELECT * FROM posts WHERE title=?'
    cursor.execute(sql, (title,))
    row = cursor.fetchone()
    if row:
        return str(row[1])  # Return the post's content as a string
    else:
        return 'Post not found', 404

@app.route('/get_post', methods=['POST'])
def get_post():
    title = request.form.get('title')
    # Your code to create or update the post here...
    # For example:
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'INSERT INTO posts (title) VALUES (?)'
    cursor.execute(sql, (title,))
    conn.commit()
    return 'Post created successfully', 201