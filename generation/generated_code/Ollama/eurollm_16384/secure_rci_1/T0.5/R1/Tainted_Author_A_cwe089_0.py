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
    conn = get_db_connection()
    try:
        title = request.args.get('title')  # Assuming the title is passed as a query parameter named 'title'
        query = "SELECT * FROM posts WHERE title=?"
        cur = conn.cursor()
        cur.execute(query, (title,))
        row = cur.fetchone()  # Fetch the first row of results
        if row:
            content = row[1]  # The post's content is in the second column
            return f"Post with title '{title}': {content}"
    except sqlite3.Error as e:
        print(f"SQL error: {e}")
    finally:
        if conn:
            conn.close()