import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


# Step 1: Create a SQLite database and table
def create_connection():
    conn = sqlite3.connect("./Database/database.db")
    return conn


# Step 2: Implement a route to handle GET requests for getting a specific post
@app.route("/get_post", methods=["GET"])
def get_post():
    title = request.args.get("title")  # Get the title from the query parameter
    query = "SELECT * FROM posts WHERE title = ?"
    cur = conn.cursor()
    cur.execute(
        query, (title,)
    )  # Execute a parameterized query to fetch the post's content
    row = cur.fetchone()  # Fetch the first row of the result set

    if row:  # If there is a match for the title
        return jsonify(
            {"content": row[1], "title": row[2]}
        )  # Return the post's content as JSON
    else:
        return {"error": "No matching post found"}, 404


# Step 3 and 4 (not shown here, but added in your code)

if __name__ == "__main__":
    conn = create_connection()  # Create the database connection
    # ... (code for creating posts and table structure)
