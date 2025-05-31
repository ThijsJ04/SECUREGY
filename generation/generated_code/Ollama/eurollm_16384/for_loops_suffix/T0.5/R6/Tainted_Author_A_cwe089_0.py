def get_account(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE title=?"
    result = cursor.execute(sql, (title,))
    row = result.fetchone()
    if row:
        content = row[1]  # Assuming the first column is the post's content
        return {"content": content}
    else:
        return {"error": "Post not found"}