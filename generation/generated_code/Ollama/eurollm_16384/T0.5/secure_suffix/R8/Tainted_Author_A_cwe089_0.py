import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get-post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    conn = get_db_connection()
    try:
        title = request.args.get("title")
        if not title or title == "all":
            query = "SELECT * FROM posts"
            cursor = conn.execute(query)
            rows = cursor.fetchall()
            return jsonify([dict(row) for row in rows])
        else:
            query = f"SELECT content FROM posts WHERE title='{title}'"
            cursor = conn.execute(query)
            result = cursor.fetchone()
            if result is None:
                return jsonify({"message": "Post not found"}), 404
            else:
                post_content = result[0] if len(result) == 1 else "No content"
                return jsonify({"post_content": post_content})
    except sqlite3.Error as e:
        return jsonify({"message": str(e)}), 500
    finally:
        conn.close()
