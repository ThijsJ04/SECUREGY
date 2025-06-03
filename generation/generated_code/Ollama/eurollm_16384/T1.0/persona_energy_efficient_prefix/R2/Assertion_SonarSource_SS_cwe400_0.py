import re
from flask import request

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex_str = request.form["regex"]  # Get regex from form data
    data_str = request.form["data"]  # Get data from form data

    match = re.search(regex_str, data_str)

    if match:
        return f"Match found at index {match.start()}: {data_str[match.start() : match.end()]}"
    else:
        return "No match found"
