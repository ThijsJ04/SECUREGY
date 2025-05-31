import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()  # Call this function to establish connection
    title = request.args.get('title')  # Get the title from the GET parameter
    query = 'SELECT * FROM posts WHERE title=? ORDER BY id DESC LIMIT 1'
    cur = conn.cursor()
    cur.execute(query, (title,))  # Execute the query with the title as a parameter
    row = cur.fetchone()  # Fetch one row of data from the result
    if not row:  # Check if there's no match for the title
        return jsonify({"error": "Post not found"}), 404
    post_content = row[1]  # Extract the post content
    conn.close()  # Close the connection
    return jsonify({"post_id": row[0], "content": post_content})