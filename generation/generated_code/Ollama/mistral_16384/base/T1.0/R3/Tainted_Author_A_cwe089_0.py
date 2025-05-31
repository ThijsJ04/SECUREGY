from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post')
def get_account():
    title = request.args.get('title', None)
    if title is None:
        return "Missing 'title' parameter", 400

    try:
        with get_db_connection() as conn:
            cur = conn.execute("SELECT content FROM Posts WHERE title = ?", (title,))
            post = cur.fetchone()
            if post is None:
                return "Post not found.", 404

            return jsonify({"content": post["content"]})
    except sqlite3.Error as err:
        print(err)
        return "Database error.", 500