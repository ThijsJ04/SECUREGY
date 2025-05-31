@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')
    conn = get_db_connection()
    query = "SELECT * FROM posts WHERE title='{}';".format(title)
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    if row:
        return str(row[1])  # Return the post's content as a string
    else:
        return "Post not found"