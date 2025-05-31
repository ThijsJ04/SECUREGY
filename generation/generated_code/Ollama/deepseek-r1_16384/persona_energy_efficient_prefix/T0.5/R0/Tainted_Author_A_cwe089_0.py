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
    # Connect to database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Extract title parameter from request
    title = request.args.get('title', '').strip().lower()  # Using lower for case-insensitive search

    try:
        # Query the database for matching post
        query = "SELECT content FROM posts WHERE title = ?"
        cursor.execute(query, (title,))

        # Fetch all possible matches
        results = cursor.fetchall()

        if not results:
            conn.close()
            return jsonify({'error': 'Post not found'}), 404

        # Return the content of the first matching post
        post_content = results[0]['content']
        return jsonify({'content': post_content}), 200

    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)