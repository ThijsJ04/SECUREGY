from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = "your_regex_pattern"  # hardcoded regex pattern
    data = "your_data_to_search"  # hardcoded data to search in

    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
