@app.route('/get_post', methods=['GET'])
def get_account():
    title = request.args.get('title')  # Get the title from the URL query parameters
    query = "SELECT * FROM posts WHERE title = ?"
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, (title,))
    row = cur.fetchone()
    conn.close()
    return row[1]  # Return the post's content as JSON or string