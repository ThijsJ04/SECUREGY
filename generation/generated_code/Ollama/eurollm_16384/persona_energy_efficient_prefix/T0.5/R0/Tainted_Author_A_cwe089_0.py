def get_account(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM posts WHERE title=?"
    cursor.execute(query, (title,))  # Add the title to the query
    row = cursor.fetchone()
    if row:
        return {"content": row[1], "id": row[2]}
    else:
        return {"error": "Post not found."}