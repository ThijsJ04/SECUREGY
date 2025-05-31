from flask import jsonify, request

def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()
    title = request.args.get('title')
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
    post_content = cursor.fetchone()['content']
    cursor.close()
    conn.close()
    return jsonify({'content': post_content})