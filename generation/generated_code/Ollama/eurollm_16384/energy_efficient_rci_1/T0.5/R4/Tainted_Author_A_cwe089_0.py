import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('Database/database.db')
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
    query = f"SELECT * FROM posts WHERE title = '{title}'"
    cursor.execute(query)
    row = cursor.fetchone()
    if row:
        return str(row[0])  # Return the post's content as a string
    else:
        return "Post not found", 404


@app.route('/get_post', methods=['POST'])
def create_account():
    '''
    Create a new post with the title from the request body.
    Return the post's ID.
    '''
    conn = get_db_connection()
    cursor = conn.cursor()
    title = request.json['title']
    query = "INSERT INTO posts (title) VALUES (?)"
    cursor.execute(query, (title,))
    conn.commit()
    row_id = cursor.lastrowid
    return str(row_id), 201