def get_post(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE title=?"
    result = cursor.execute(sql, (title,))
    post = result.fetchone()
    conn.close()
    return {'post': post}