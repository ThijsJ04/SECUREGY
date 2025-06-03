from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    data = request.get_json()
    regex_pattern = data["regex"]
    target_string = data["data"]
    if re.search(regex_pattern, target_string):
        return "Match found"
    else:
        return "No match found"
