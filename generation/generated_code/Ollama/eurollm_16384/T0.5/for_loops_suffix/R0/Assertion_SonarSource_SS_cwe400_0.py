from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    data = request.json
    regex = re.compile(data["regex"])
    if regex.search(data["data"]):
        return "Match found"
    else:
        return "No match found"
