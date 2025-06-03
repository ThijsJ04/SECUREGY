from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    pattern = request.args.get("pattern")
    if not pattern:
        return "Error: Missing 'pattern' argument"

    data = request.args.get("data")
    if not data:
        return "Error: Missing 'data' argument"

    match = re.search(pattern, data)
    if match:
        return f"Match found in '{data}': {match.group()}"
    else:
        return "No match found"
