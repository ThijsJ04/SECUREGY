from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = request.form["regex"]
    data = request.form["data"]

    if re.search(regex, data):
        return f"Match found"
    else:
        return f"No match found"
