import sqlalchemy
from flask import Flask, request
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

app = Flask(__name__)
Base = automap_base()
Base.prepare(
    bind=sqlalchemy.create_engine('sqlite:///Database/database.db')
)
session = Session(bind=Base.sessionmaker().Session())

@app.route('/get_post', methods=['GET'])
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    try:
        title = request.args.get('title')
        if not title or not isinstance(title, str):
            return 'Error: Title is required', 400

        posts = session.query(Base.classes).filter_by(title=title)
        if len(posts) == 0:
            return f'No post found with title "{title}"', 404

        return posts[0].content, 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()