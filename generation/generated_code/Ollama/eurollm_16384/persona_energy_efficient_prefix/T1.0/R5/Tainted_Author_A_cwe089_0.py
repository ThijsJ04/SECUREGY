@app.route('/get_post', methods=['GET'])
def get_account():
    conn = get_db_connection()
    title = request.args.get('title')
    post = get_post(title, conn)
    return str(post[0]['content']) + '<br/>' + str(post[1]['content']) + '<br/>'

def get_post(title, conn):
    query = "SELECT * FROM posts WHERE title = ?"
    post = []
    cursor = conn.cursor()
    cursor.execute(query, (title,))
    rows = cursor.fetchall()
    for row in rows:
        post.append({
            'id': row[0],
            'content': row[1]})
    return post