import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    try:
        regex = request.args.get("regex")
        data = request.args.get("data")
    except ValueError:
        return "Invalid request parameters", 400

    if not regex or not data:
        return "Missing regex or data", 400

    pattern = re.compile(regex)
    match = pattern.search(data)

    if match:
        return f"Match found: {match.group()}"
    else:
        return "No match found"
