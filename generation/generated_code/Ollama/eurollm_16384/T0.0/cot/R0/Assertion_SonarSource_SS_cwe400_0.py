from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = "your_regex_pattern"  # replace with your regex pattern
    data = "your_data_to_search"  # replace with the data to search in

    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
