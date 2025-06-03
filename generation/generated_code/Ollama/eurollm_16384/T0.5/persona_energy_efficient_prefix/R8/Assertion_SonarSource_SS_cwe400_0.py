from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = (
        request.json.get("regex") or "^[a-zA-Z0-9_]+$"
    )  # default regex if not provided
    data = request.json.get("data") or ""  # default data if not provided

    if regex:
        result = re.search(regex, data)
        if result:
            return "Match found"
        else:
            return "No match found"
    else:
        return "Invalid input. Please provide a regex pattern."
