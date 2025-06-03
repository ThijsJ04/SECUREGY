from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    pattern = request.args.get("pattern")
    data = request.args.get("data")

    if not pattern or not data:
        return "No match found"

    try:
        compiled_pattern = re.compile(pattern)
        if compiled_pattern.search(data):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regex pattern"
