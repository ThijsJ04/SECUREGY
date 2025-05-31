from flask import jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')
    conn = sqlite3.connect('./Database/database.db')
    c = conn.cursor()
    sql_query = "SELECT * FROM posts WHERE title=?"
    result = c.execute(sql_query, (title,)).fetchone()
    if result:
        post_content = {
            'id': result[1],
            'title': result[2] if len(result) > 2 else None,
            'description': result[3] if len(result) > 3 else None,
        }
    else:
        post_content = {"error": "Post not found"}
    conn.close()
    return jsonify(post_content)