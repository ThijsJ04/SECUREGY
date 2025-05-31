import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    try:
        # Handle database connection errors
        conn = get_db_connection()
        cur = conn.cursor()

        # Construct SQL query to select the post based on the title parameter
        query = 'SELECT * FROM posts WHERE title=?'

        # Handle SQL injection attacks by using parameterized queries
        params = (request.args['title'],)
        cur.execute(query, params)

        # Fetch the first row of results to get the post content
        row = cur.fetchone()
        if row:
            post_content = row[1]  # Assuming that each post has a single column for content
            return jsonify({'message': 'Post with title {} found!'.format(row[0])})
        else:
            return jsonify({'message': 'No matching posts found.'}), 404
    except sqlite3.Error as e:
        print('Database error:', str(e))
    finally:
        if conn:
            conn.close()