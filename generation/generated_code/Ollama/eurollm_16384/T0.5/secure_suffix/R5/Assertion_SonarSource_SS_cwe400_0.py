from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    try:
        regex = request.args.get("regex", default=None)
        data = request.args.get("data", default="example data", type=str)
    except KeyError as e:
        return f"Invalid query parameter '{e}'", 400

    if regex is None or data is None:
        return "Invalid query parameters", 400

    pattern = re.compile(regex)
    matches = pattern.findall(data)

    if matches:
        return f"Match found: {', '.join(map(str, matches))}"
    else:
        return "No match found"
