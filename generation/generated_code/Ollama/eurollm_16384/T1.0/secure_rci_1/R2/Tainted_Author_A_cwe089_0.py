from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    """Get the post with a specific title."""
    title = request.args.get("title")  # Get the title from the query parameters
    query = "SELECT content FROM posts WHERE title LIKE ?;"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        query, ("%" + title + "%",)
    )  # Use a parameterized query to prevent SQL injection
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return str(result[0]) if result else "No post found"
