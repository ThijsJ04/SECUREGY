def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM posts WHERE title=?", (title,))
    result = cur.fetchone()
    if result:
        return result['content']
    else:
        return "Post not found"