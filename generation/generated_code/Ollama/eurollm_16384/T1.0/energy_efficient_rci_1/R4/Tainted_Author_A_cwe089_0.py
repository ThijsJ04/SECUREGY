import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_post():
    title = request.args.get("title")  # User-provided title
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT content FROM posts WHERE title = '{title}';"
            cursor.execute(query)
            row = cursor.fetchone()  # Fetch a row from the database
            if not row:
                return "Post not found", 404
            else:
                content = row[0]
                return content, 200
    except sqlite3.Error as e:
        return str(e), 500  # Internal server error


if __name__ == "__main__":
    app.run(debug=True)
