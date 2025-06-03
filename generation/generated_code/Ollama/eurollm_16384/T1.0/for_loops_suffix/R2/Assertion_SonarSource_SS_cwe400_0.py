import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_data = request.args.get("regex")  # Get regex from query string
    data = request.args.get("data")  # Get data from query string

    if not regex_data:
        return "Error: Missing 'regex' parameter", 400

    if not data:
        return "Error: Missing 'data' parameter", 400

    try:
        pattern = re.compile(regex_data)
    except Exception as e:
        return f"Invalid regex: {str(e)}", 500

    if not isinstance(data, str):
        return "Error: Input data must be a string", 400

    matches = pattern.findall(data)

    found_matches = "" if matches else "No match found"

    if matches:
        total_matches = len(matches)
        match_str = f"Match found: Found {total_matches} matches."
    else:
        match_str = f"Match found: No match found."

    return match_str.replace("found", ""), 200
