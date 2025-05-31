def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT content FROM posts WHERE title=?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result['content']
    else:
        return 'Post not found'