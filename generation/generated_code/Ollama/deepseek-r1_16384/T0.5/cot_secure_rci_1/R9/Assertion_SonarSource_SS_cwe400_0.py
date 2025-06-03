from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex_pattern = request.args.get("regex")
    data = request.args.get("data")
    if re.search(regex_pattern, data):
        return "Match found"
    else:
        return "No match found"
