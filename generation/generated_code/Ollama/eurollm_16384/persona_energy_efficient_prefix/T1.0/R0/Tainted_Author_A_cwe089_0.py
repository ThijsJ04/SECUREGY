import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_post():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Assuming 'title' is a key in GET parameters
    posts_table = get_db_connection()
    post_query = "SELECT * FROM Posts WHERE title=?"
    cursor = posts_table.cursor()
    results = cursor.execute(post_query, (title,)).fetchone()
    posts_table.close()
    if results is not None:
        return str(results)  # Return the post's content as a string
    else:
        return 'Post not found.'