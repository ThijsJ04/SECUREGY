@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')

    if not title:
        return "Error: Missing title parameter"

    conn = get_db_connection()
    cursor = conn.cursor()

    post_sql = 'SELECT * FROM posts WHERE title=? ORDER BY id DESC LIMIT 1'
    cursor.execute(post_sql, (title,))
    result = cursor.fetchone()

    if not result:
        return "No post found with the specified title"
    else:
        conn.close()
        return str(result[1])  # Return the post's content