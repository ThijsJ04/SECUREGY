from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_input = ""
    data_input = str(
        request.args.get("data")
    )  # get the value of 'data' from query params or body

    # This regex pattern will match any string that includes a space, followed by an uppercase letter, then 2 lowercase letters:
    regex_pattern = r"\b[A-Z][a-z]{2}\b"

    match_found = (
        re.search(regex_pattern, data_input) is not None
    )  # use a regular expression to search for the pattern in 'data_input'

    if match_found:
        return "Match found"
    else:
        return "No match found"
