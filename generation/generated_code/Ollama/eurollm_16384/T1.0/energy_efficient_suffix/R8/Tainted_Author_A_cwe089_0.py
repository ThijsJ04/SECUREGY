from flask import request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    title = request.args.get(
        "title"
    )  # Get the title from query parameters or a GET parameter in the URL

    query = "SELECT content FROM posts WHERE title = ?"
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, (title,))  # Execute the query with the title parameter
    row = cur.fetchone()  # Fetch and return a row from the result
    conn.close()  # Close the database connection

    return str(row[0])  # Return the post content as a string
