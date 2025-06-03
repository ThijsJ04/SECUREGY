from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Replace ''.join([i.split() for i in title.split(' ')]) with a better solution
def get_db_connection():
    conn = sqlite3.connect("./Database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/get_post", methods=["GET"])
def get_account():
    try:
        # Get the title from the request parameters
        title = request.args.get("title")  # Assume 'title' is the key in query string

        with get_db_connection() as conn:
            cur = conn.cursor()
            # Your existing code here...

    except sqlite3.Error as e:
        print(e)
        return jsonify(
            {"error": "Database connection failed"}
        ), 500  # Return a 500 status code for internal server error
    else:
        # Your existing code here...
        conn.close()

        return jsonify(
            {"title": title, "content": content}
        )  # Return the post's content in JSON format
