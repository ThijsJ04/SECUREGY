@app.route('/get_post')
def get_account():
    title = request.args.get('title', default='Default Title')
    conn = get_db_connection()
    query = 'SELECT content FROM posts WHERE title = ?'
    cur = conn.cursor()
    cur.execute(query, (title,))
    row = cur.fetchone()
    if row:
        return str(row[0])
    else:
        return 'Post not found', 404