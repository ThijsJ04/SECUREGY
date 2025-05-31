import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')  # Update path to your database file as needed
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    params = {"title": request.args.get("title")}  # Get the parameter from the GET request
    try:
        conn = get_db_connection()
        query = "SELECT * FROM posts WHERE title=?"
        result = conn.execute(query, (params["title"],))
        row = result.fetchone()  # Fetch the first row of the query result
        content = f"Post Title: {row['title']}\nPost Content: {row['content']}" if row else "No post found"
    except sqlite3.Error as e:
        if conn:
            conn.close()  # Close the database connection when an error occurs
        print(f"Error getting post: {e}")
    finally:
        return content