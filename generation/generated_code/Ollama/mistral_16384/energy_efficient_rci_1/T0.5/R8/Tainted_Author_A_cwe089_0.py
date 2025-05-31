from sqlite3 import OperationalError
import psycopg2

@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters ('title').
    Return the post's content.
    '''
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        title = request.args.get('title')
        cursor.execute("SELECT content FROM posts WHERE title=?", (title,))
        result = cursor.fetchone()
        if result:
            return result['content']
        else:
            return "Post not found.", 404
    except OperationalError as e:
        return str(e), 500
    finally:
        conn.close()