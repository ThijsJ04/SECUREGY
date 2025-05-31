from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')  # assuming the database file is already created
    return conn

@app.route('/get_post', methods=['GET'])
def get_account(title):
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    conn = get_db_connection()  # connect to the database using the function defined above
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts WHERE title=?', (title,))
    row = cursor.fetchone()
    if row:  # check if a row is fetched
        return {'post': row}
    else:
        return 'Post not found'