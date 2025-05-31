import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Assuming 'title' is a GET parameter
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE title=?"
    result = cursor.execute(sql, (title,))  # Using a tuple to pass the title
    post = result.fetchone()  # Fetching one row of data
    conn.close()  # Closing the database connection
    return f"Post found: {post[1]}"