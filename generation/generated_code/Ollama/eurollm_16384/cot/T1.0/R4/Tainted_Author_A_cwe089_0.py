@app.route('/get_post', methods=['GET'])
def get_account():
    conn = get_db_connection()
    query = "SELECT content FROM posts WHERE title = ?"
    db_cursor = conn.cursor()
    db_cursor.execute(query, (request.args['title'],))
    result = db_cursor.fetchone()
    post = None if not result else result[0]  # Handle the case where no results are found

    return jsonify({"post": post})