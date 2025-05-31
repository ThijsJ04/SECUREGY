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
    try:
        title = request.args.get('title')  # Get the requested title parameter
        query = "SELECT * FROM posts WHERE title=?"
        with conn as cursor:
            cursor.execute(query, (title,))  # Execute the query with the provided title
            result = cursor.fetchone()       # Fetch one row from the result set
    except sqlite3.OperationalError as e:
        return "Invalid SQL", 400
    if not result:
        return "Post not found", 404
    post_content = result[1]  # Retrieve the post content (post_id is assumed to be column index 1)
    return str(post_content), 200