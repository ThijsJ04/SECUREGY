from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = (
        request.json.get("regex") or ".*"
    )  # default regex if not provided in request
    data = request.json.get("data") or ""

    if regex and data:
        match = re.search(regex, data)
        if match:
            return f"Match found at position {match.start()} with length {len(match.group())}"
        else:
            return "No match found"
    else:
        return "Invalid request", 400
