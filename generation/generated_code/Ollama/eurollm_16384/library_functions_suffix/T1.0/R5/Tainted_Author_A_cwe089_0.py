def get_post(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT content FROM posts WHERE title=?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None