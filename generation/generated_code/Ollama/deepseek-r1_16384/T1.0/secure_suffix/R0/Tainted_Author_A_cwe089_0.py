import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post")
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title", "Not found")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts WHERE title LIKE ?", (f"{title}%",))

    post = cursor.fetchone()

    if not post:
        return jsonify({"message": f"Post with title {title} not found"}), 404

    content = str(post["content"])

    conn.close()

    return jsonify({"content": content})


if __name__ == "__main__":
    app.run(debug=True)
