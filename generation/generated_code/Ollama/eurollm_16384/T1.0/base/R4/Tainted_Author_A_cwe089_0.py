import sqlite3
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)


# Initialize the database and models
with app.app_context():
    db.create_all()


# Function to get a post by title
def get_post_by_title(title):
    query = Post.query.filter_by(title=title).first()
    if query:
        return {"content": query.content}
    else:
        return None


# Function to authenticate a user and retrieve their posts
def get_user_posts(username, password):
    connection = db.engine.connect()
    cursor = connection.cursor()

    query = User.query.filter_by(username=username).first()
    if query:
        post_ids = Post.query.join(User).filter_by(user_id=query.id).all()
        return [
            {"content": post["content"]}
            for post in db.session.query(Post).filter(Post.id.in_(post_ids))
        ]
    else:
        cursor.close()
        connection.close()
        return []


# Route to handle user authentication and retrieve posts
@app.route("/authenticate", methods=["POST"])
def authenticate():
    username = request.form["username"]
    password = request.form["password"]

    query = User.query.filter_by(username=username).first()
    if query:
        if query.password == password:
            return {"message": "Authentication successful"}
        else:
            return {"message": "Incorrect username or password"}
    else:
        return {"message": "Username not found"}


@app.route("/get_post", methods=["GET"])
def get_post():
    title = request.args.get("title")
    post = get_post_by_title(title)
    if post:
        return jsonify({"content": post})
    else:
        # For testing purposes, return a dummy response with an error message
        return jsonify({"message": "Post not found"}), 404


@app.route("/user_posts", methods=["GET"])
def user_posts():
    username = request.args.get("username")
    posts = get_user_posts(username, "password")
    return jsonify({"posts": posts})


if __name__ == "__main__":
    app.run()
