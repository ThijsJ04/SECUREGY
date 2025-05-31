def get_account():
    conn = get_db_connection()
    cursor = conn.cursor()
    title = request.args.get('title')
    query = "SELECT content FROM posts WHERE title=?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    if result:
        return str(result[0])
    else:
        return 'Post not found'