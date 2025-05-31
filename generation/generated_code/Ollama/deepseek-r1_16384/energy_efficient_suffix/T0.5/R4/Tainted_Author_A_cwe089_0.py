import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''

    try:
        # Check if title parameter is provided in the request
        title = request.args.get('title', '')
        if not title:
            return jsonify({'error': 'Title parameter is required'}), 400

        with get_db_connection() as conn:
            cursor = conn.cursor()

            # Query to fetch post content by title
            query = "SELECT content FROM posts WHERE title LIKE ?"
            cursor.execute(query, (title,))

            # Check if the post exists
            post = cursor.fetchone()
            if not post:
                return jsonify({'error': 'Post not found'}), 404

            # Return the content in JSON format
            return jsonify({
                'content': post['content'],
                'message': 'Post retrieved successfully'
            }), 200

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({'error': str(e)}), 500