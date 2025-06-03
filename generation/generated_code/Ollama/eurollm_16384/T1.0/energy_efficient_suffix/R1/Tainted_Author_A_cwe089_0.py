import sqlite3
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = get_db_connection()


# Create a model for Post with one column 'title'
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db.db_url()
db.init_app(app)


@app.route("/get_post")
def get_account():
    # Get the title from request's parameters
    title = request.args.get("title", default="Default Post Title")

    if not title:
        return "Missing required parameter 'title'", 400

    post = Post.query.filter_by(title=title).first()

    if post is None:
        return f"Post with title '{title}' not found", 404

    return post.content, 200


# Example usage to create a new post:
@app.route("/create_post", methods=["POST"])
def create_post():
    title = request.json["title"]
    content = request.json["content"]

    if not title or not content:
        return "Missing required parameters 'title' and 'content'", 400

    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()

    return f"Post created successfully: {new_post.title}", 201


if __name__ == "__main__":
    app.run(debug=True, port=3000)
