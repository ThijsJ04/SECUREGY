import sqlite3
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///Database/database.db"  # Using SQLAlchemy instead of sqlite3 directly for connection
)
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(
        db.String(100), nullable=False
    )  # Set column name and type for title
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post({self.title!r}, {self.content})"


@app.route("/get_post", methods=["GET"])
def get_account():
    """
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    """
    title = request.args.get("title")  # Get title from GET request parameters

    with db.session_transaction():
        post = Post.query.filter_by(title=title).first()  # Query posts by title
        if post is None:
            return (
                "Post not found",
                404,
            )  # Return a JSON response with the status code and message

    return str(post), 200  # Convert Post object to string and return it as JSON
