from flask import request, jsonify
import sqlite3

app = Flask(__name__)
db_connection = (
    get_db_connection()
)  # This function will be used to establish a database connection


def get_post(title):
    """
    Get the post with a specific title.
    Args:
        title (str): The title of the post you want to retrieve.
    Returns:
        A JSON response containing the post's content if it exists, otherwise None.
    """
    cur = db_connection.cursor()  # Create a cursor object
    query = "SELECT * FROM posts WHERE title = ?"
    cur.execute(query, (title,))  # Execute the query with the provided title
    row = cur.fetchone()  # Fetch one row of data from the query result
    if row:  # If a row is fetched, there's a post with that title
        return jsonify(dict(row))  # Return the post's content as a JSON response
    else:
        return {
            "message": "No post found with that title."
        }, 404  # If no row is fetched, return an error message and HTTP 404 status code


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title")  # Get the title parameter from the request
    return get_post(title)  # Call the get_post function with the provided title
