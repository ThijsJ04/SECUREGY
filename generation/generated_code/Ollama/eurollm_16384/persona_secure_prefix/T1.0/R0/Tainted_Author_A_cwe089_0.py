def get_account():
    conn = get_db_connection()
    query = 'SELECT * FROM posts WHERE title=?'
    params = (request.args.get('title'),)  # Get the title from the request's parameters
    rows = conn.execute(query, params)  # Execute the query with the parameter
    for row in rows:
        return {'content': row['content']}  # Return the post's content if found
    conn.close()  # Close the database connection when done