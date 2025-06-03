from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = request.json.get("regex")
    data = request.json.get("data")

    if regex and data:
        for item in data:
            if re.search(regex, item):
                return "Match found"
        return "No match found"
    else:
        return "Invalid input", 400
