import sqlite3
from flask import request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()
    cursor = conn.cursor()

    title = request.args.get('title')

    if title:
        query = "SELECT * FROM posts WHERE title=?;"
        cursor.execute(query, (title,))
        record = cursor.fetchone()

        if record:
            return str(record[1])  # return post's content
    else:
        return 'Title is required', 400

    conn.close()