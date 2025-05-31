import sqlite3
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Database/database.db"
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/get_post')
def get_post():
    # Get the post's title from the request parameters
    title = request.args.get("title")

    if not title:
        return "Please provide a title", 400

    with db.transaction():
        post = Post.query.filter_by(title=title).first()
        if post:
            return {"content": post.content}
        else:
            return {"message": "Post not found"}, 404