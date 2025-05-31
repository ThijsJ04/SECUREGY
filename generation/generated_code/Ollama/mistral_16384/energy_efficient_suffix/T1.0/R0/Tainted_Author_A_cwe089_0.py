@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM Posts WHERE title=?", (title,))
    result = cursor.fetchone()
    if result:
        return result['content']
    else:
        return "Post not found.", 404