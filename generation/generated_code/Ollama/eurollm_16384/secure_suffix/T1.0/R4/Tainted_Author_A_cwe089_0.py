@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Assuming that the 'title' parameter is included in the GET request

    if not title:
        return 'Title is required', 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(query, (title,))  # Use parameterized queries to prevent SQL injection
    result = cursor.fetchone()  # Fetch the first result from the query

    if not result:
        return 'Post not found', 404

    post_content = str(result[1]) + " - " + str(result[2])
    conn.close()

    return {'post': post_content}, 200  # Return the post's content as a JSON object