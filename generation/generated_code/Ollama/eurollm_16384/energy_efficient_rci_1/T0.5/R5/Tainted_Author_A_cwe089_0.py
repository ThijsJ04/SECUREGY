@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')
    if not title:
        return 'Title is required', 400

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE title = ?"
    cursor.execute(sql, (title,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return 'Post not found', 404

    content = row['content']
    return content