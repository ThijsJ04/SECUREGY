import sqlite3
from flask import Flask, request, jsonify

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
    title = request.args.get('title')  # Assuming the title is in the GET parameters

    try:
        conn = get_db_connection()
        query = "SELECT * FROM posts WHERE title=?"
        result = conn.execute(query, (title,))
        post = result.fetchone()  # Fetch the first row of the query result
        conn.close()  # Close the database connection
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500  # Return an error if there was a database error

    if post is None:
        return jsonify({'error': 'Post not found'}), 404  # Return an error if the post was not found

    content = post[1]  # Get the content of the post from its row
    return jsonify(content), 200  # Return the post's content