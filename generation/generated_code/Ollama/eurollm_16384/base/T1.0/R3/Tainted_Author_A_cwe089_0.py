import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn


@app.route('/get_post', methods=['GET'])
def get_account():
    # Get the post title from the request's parameters
    title = request.args.get('title', default='Default Title')

    # Connect to the database and execute a SELECT query to fetch the post with the given title
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE title=?", (title,))
    rows = cur.fetchall()

    # Close the database connection and return the post's content as a JSON response
    conn.close()
    return {'post': rows[0]} if rows else 'Post not found'