import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    # Retrieve the required data from the request parameters or query string
    title = request.args.get(
        "title"
    )  # Get the title parameter if it exists in the URL query string

    if not title:
        return "Title is required", 400

    # Establish a connection to your SQLite database and execute an appropriate SQL query
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f'SELECT * FROM posts WHERE title="{title}";'  # Execute the query with the specified title

    # Fetch the results of the query and return them as JSON
    results = cursor.fetchall()
    conn.close()  # Close the database connection to free up resources
    return jsonify({"data": [result for result in results]})
