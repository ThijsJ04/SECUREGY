import sqlite3
from flask import request, jsonify

@app.route('/get_post', methods=['GET'])
def get_account():
    # Get the title from the request parameters
    title = request.args.get('title')

    # Establish a database connection
    conn = sqlite3.connect('./Database/database.db')
    cursor = conn.cursor()

    # Query the database for posts with the specified title
    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))
    rows = cursor.fetchone()

    if rows:
        post_content = rows[1]  # Assuming the first column is the content of the post
        return jsonify({'status': 'success', 'post_content': post_content})
    else:
        return jsonify({'status': 'failure', 'message': f"No post found with title {title}."}), 404

    # Close the database connection
    conn.close()