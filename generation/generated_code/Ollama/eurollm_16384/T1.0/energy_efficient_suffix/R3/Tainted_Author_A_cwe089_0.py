from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.

    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title")

    # SQL query to select the post
    query = "SELECT * FROM posts WHERE title=?"
    results = []

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (title,))
            row = cursor.fetchone()
            if row:
                results.append(row)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return "An error occurred", 500

    return str(results)[1:-1], 200
