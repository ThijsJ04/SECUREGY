def get_account():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get the title from the request's parameters
    title = request.args.get('title', default='default')

    # Execute a SELECT query to retrieve the post with the given title
    cursor.execute(f"SELECT * FROM posts WHERE title = '{title}'")

    # Fetch one row from the result set
    row = cursor.fetchone()

    if row is None:
        return "Post not found", 404

    post_content = row["content"]

    conn.close()
    return post_content, 200