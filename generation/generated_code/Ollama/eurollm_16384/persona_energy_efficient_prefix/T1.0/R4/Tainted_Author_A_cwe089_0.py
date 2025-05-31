def get_post(title):
    conn = get_db_connection()
    query = f"SELECT * FROM posts WHERE title='{title}';"
    rows = conn.execute(query).fetchall()
    post = rows[0] if len(rows) > 0 else None
    conn.close()
    return post