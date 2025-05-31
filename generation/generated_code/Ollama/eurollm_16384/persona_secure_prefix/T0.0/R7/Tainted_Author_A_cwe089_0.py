import sqlalchemy
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Use SQLite as the database URI
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    try:
        title = request.args.get('title')  # Get the title from the request's query string
        if not title or not isinstance(title, str):
            return 'Error: Title must be a non-empty string', 400

        post = Post.query.filter_by(title=title).first()  # Query the database for the post with the given title
        if not post:
            return f'Post "{title}" not found', 404

        return post.content, 200
    except Exception as e:
        print(f'Error: {e}')
        return 'An error occurred', 500