import sqlite3
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///database.db"  # configure the database URI
)
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # column for the post's title
    content = db.Column(db.Text, nullable=False)  # column for the post's content

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"


@app.route("/get_post", methods=["GET"])
def get_post():
    # Get the title from the request's parameters and query for a post with that title
    title = request.args.get(
        "title"
    )  # assuming the title is in the URL or query string
    posts = Post.query.filter_by(title=title).first()

    if not posts:  # if no post found with the given title
        return "No post found", 404

    return str(posts)  # return the post's content as a string
