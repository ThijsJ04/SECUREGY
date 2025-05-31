from sqlite3 import Error

@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)

    if not title:
        return "Error: Title is required", 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
        row = cursor.fetchone()

        if not row:
            return "Error: Post with that title does not exist", 404

        result = row['content']
    except Error as e:
        conn.close()
        return str(e)

    conn.close()
    return result