from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_query = request.args.get("regex")
    data_content = request.args.get("data")

    if regex_query and data_content:
        match_found = re.search(regex_query, data_content)
        if match_found:
            return f"Match found: '{regex_query}' found at positions {match_found.start()} to {match_found.end()} in the string."
        else:
            return "No match found."
    else:
        return "Invalid input, please provide a regex and data content."
