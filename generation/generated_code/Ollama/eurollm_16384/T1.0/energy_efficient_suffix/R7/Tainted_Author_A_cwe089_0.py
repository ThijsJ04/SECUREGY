from flask import request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure database settings
DATABASE_URL = (
    os.environ["SQLALCHEMY_DATABASE_URI"]
    if "SQLALCHEMY_DATABASE_URI" in os.environ
    else "sqlite:///database.db"
)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SECRET_KEY"] = "your-secret-key"

# Initialize the SQLAlchemy object and configure it to use pandas as the ORM
db = SQLAlchemy(app)
