@app.route('/get_post')
def get_account():
    title = request.args.get('title', default='All posts')
    query = "SELECT * FROM Posts WHERE title=?"
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, (title,))
    row = cur.fetchone()
    post = row[2] if row else None
    conn.close()
    return post or "Post not found"