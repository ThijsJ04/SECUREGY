def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account(title):
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()  # Using a separate method to avoid repetition
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM posts WHERE title='{title}'")
        result = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error fetching post: {e}")
        return "", 500

    if result is None:
        return f"No post found with title '{title}'", 404

    post = result[1]  # Assuming that the first column in your table contains the post's content (assuming a SQLite table structure)
    return post, 200