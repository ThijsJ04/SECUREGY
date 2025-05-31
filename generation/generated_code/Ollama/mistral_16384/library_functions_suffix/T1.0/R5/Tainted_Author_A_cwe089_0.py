def get_account():
       title = request.args.get('title')
       conn = get_db_connection()
       cursor = conn.cursor()
       cursor.execute("SELECT content FROM Post WHERE title = ?", (title,))
       result = cursor.fetchone()
       return str(result['content']) if result else "No post found with the given title."