from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")
    if regex and data:
        match = re.search(regex, data)
        if match:
            return "Match found"
        else:
            return "No match found"
    else:
        return "Error: Please provide both regex pattern and data"
