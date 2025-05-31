@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    if not title:
        return {'error': 'Missing required parameter "title"'}, 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    result = cursor.fetchone()
    if not result:
        return {'error': 'No post found with the given title'}, 404

    conn.close()
    return result['content']