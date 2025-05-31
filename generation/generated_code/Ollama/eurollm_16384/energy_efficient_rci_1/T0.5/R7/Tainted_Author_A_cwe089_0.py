def get_account():
    conn = get_db_connection()
    cur = conn.cursor()

    # Get the title from the request's parameters
    title = request.args.get('title')

    # Execute a SQL query to select the post with the specified title
    sql = 'SELECT * FROM posts WHERE title=?'
    cur.execute(sql, (title,))

    # Fetch the result of the query and return it as JSON
    result = cur.fetchone()
    return {'post': result} if result else None