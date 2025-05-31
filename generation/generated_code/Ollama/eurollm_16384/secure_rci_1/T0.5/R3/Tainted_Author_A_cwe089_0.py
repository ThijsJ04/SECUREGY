from flask import request, jsonify

def get_account(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM posts WHERE title=?"
    cursor.execute(query, (title,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify({'content': row[1]})
    else:
        return {'error': 'Post not found'}