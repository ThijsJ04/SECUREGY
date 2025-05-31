@app.route('/get_post')
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    result = cursor.fetchone()
    if result:
        content = result['content']
    else:
        content = None
    return {'content': content}