from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_input = request.args.get("regex")
    data_input = request.args.get("data")

    if regex_input and data_input:
        # Remove any leading or trailing whitespace from the input strings
        regex_input = re.sub(r"\s+", "", regex_input).strip()
        data_input = re.sub(r"\s+", "", data_input).strip()

        # Check if the regex matches any part of the data
        if bool(re.match(regex_input, data_input)):
            return f"Match found"
        else:
            return "No match found"
    else:
        return "Missing required arguments"
