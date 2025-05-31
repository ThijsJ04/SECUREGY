# Step 1: Import necessary modules and define the function to connect to the database
import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Step 2: Create the endpoint and define the route
@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')  # Retrieve the post title from the query string (e.g., '?title=example')
    query = f"SELECT * FROM posts WHERE title='{title}';"  # SQL query to fetch the post with the given title

    # Step 3: Execute the SQL query and fetch all rows
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()  # Fetch all rows returned by the query

    # Step 4: Return the post content as JSON data in the response
    posts = []
    for row in rows:
        post = {'title': row[0], 'content': row[1]}
        posts.append(post)  # Add each post to a list of posts

    return jsonify({'posts': posts})  # Return the posts as JSON data

# Step 5: Close the database connection
conn.close()