def get_post(title):
    conn = get_db_connection()
    query = f"SELECT content FROM posts WHERE title='{title}'"
    post = conn.execute(query).fetchone()
    if post:
        return {'content': post['content']}
    else:
        return {'message': 'Post not found'}