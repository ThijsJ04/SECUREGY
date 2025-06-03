import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account(title):
    try:
        # Establish a connection to the database
        conn = get_db_connection()

        # Execute a query to retrieve the post with the given title
        result = conn.execute("SELECT * FROM posts WHERE title=?", (title,))

        # Fetch all rows from the result and return them as JSON
        data = [dict(row) for row in result]

        return jsonify({"status": "success", "data": data})
    except sqlite3.Error as e:
        # Handle any errors that occur during database operations
        return jsonify(
            {"error": str(e)}
        ), 500  # Return a 500 Internal Server Error response
    finally:
        # Close the database connection if it was established
        conn.close()
