from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_str = request.args.get("regex")
    data_str = request.args.get("data")

    # Validate the input regex and data
    if not isinstance(regex_str, str) or not re.match("^[a-zA-Z0-9._%+-]+$", regex_str):
        return "Invalid regex"
    if not isinstance(data_str, str) or len(data_str) < 1:
        return "No data provided"

    # Perform the regex search and return the result
    pattern = re.compile(regex_str)
    matches = pattern.findall(data_str)
    if matches:
        return "Match found"
    else:
        return "No match found"
