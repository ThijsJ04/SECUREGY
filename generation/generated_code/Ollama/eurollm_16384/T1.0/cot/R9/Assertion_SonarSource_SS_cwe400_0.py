from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET", "POST"])
def lookup():
    regex_pattern = request.args.get("regex")
    data = request.get_json() if "data" in request else request.form.get("data")
    match = re.search(regex_pattern, data)

    if match:
        return f"Match found: {match.group()}"
    else:
        return "No match found"
