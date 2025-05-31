def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM Posts WHERE title=?", (title,))
    result = cursor.fetchone()
    return result['content'] if result else "Post not found"