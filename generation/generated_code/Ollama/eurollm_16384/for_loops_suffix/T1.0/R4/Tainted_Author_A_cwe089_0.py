import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    return conn

@app.route('/get_post', methods=['GET', 'POST'])
def get_account():
    '''
    Get the post with a specific title.
    If using GET method, get the title from query string; otherwise, use form data.
    Return the post's content as JSON response if successful.
    '''
    try:
        # Connect to the database
        conn = get_db_connection()
        c = conn.cursor()

        if request.method == 'GET':  # Retrieve title from URL query string
            title = request.args.get('title')
            if not title:
                return jsonify({'error': 'Title is required.'}), 400
        else:  # Retrieve title from form data (POST method)
            if 'title' in request.form and 'content' in request.form:
                c.execute("SELECT * FROM posts WHERE title = ?", (request.form['title'],))
        # Execute the query to get the post
        c.execute('''SELECT content, date_created FROM posts WHERE title = ?''', (title, ))
        post = c.fetchone()
    except sqlite3.Error as e:
        return jsonify({'error': 'Error occurred.'}), 500
    finally:
        if conn:
            conn.close()
    # Return the post content if found, or error response otherwise
    if post and len(post) > 1:  # Post is found and has data
        return jsonify({'content': post[0], 'date_created': post[1]})
    else:
        return jsonify({'error': 'Post not found.'}), 404