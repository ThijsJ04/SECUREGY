import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection(table_name):
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account(title):
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection('posts')
    query = "SELECT * FROM posts WHERE title=?"
    result = conn.execute(query, (title,) )
    rows = result.fetchall()
    post = None
    if rows:
        post = rows[0]
        return {'post': post['content']}
    else:
        return {'message': 'No posts found with the specified title.'}, 500