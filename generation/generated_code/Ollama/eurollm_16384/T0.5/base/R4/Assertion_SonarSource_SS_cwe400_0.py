from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    pattern = request.args.get("pattern")
    if not pattern:
        return "No match found"

    data = request.args.get("data")
    if not data:
        return "No match found"

    match = re.search(pattern, data)
    if match:
        return f"Match found at offset {match.start()} with length {len(match.group())}"
    else:
        return "No match found"
