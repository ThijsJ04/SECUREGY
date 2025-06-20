from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")

    if not regex or not data:
        return "No match found"

    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
