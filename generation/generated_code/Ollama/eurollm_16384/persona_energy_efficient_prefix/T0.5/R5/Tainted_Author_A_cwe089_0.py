@app.route('/get_post')
def get_account():
    title = request.args.get('title', default=None)
    if not title:
        return 'Title is required'

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = f"SELECT content FROM posts WHERE title='{title}'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row:
        return str(row[0])
    else:
        return 'Post not found'