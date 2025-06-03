from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_input = request.args.get("regex")
    data_input = request.args.get("data")

    if regex_input and data_input:
        match = re.search(regex_input, data_input)
        if match:
            return "Match found"
        else:
            return "No match found"
    else:
        return "Invalid input. Please provide both regex and data."
