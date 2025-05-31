@app.route('/get_post', methods=['GET'])
def get_account():
    conn = get_db_connection()
    query = "SELECT title, content FROM posts WHERE title = ?"
    result = conn.execute(query, (request.args.get('title'),))
    post = result.fetchone()
    conn.close()
    return {'post': post} if post else None