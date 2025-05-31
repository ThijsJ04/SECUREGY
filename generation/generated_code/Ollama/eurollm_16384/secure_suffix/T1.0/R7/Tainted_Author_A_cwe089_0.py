def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    # Get the title from the request parameters
    title = request.args.get('title')

    # Query the database for the post with the given title
    conn = get_db_connection()
    query = "SELECT * FROM posts WHERE title=?"
    cur = conn.cursor()
    cur.execute(query, (title,))
    result = cur.fetchone()

    # Close the connection
    conn.close()

    return str(result)