from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = re.compile(
        request.args.get("regex")
    )  # Compile the regular expression from the request argument
    data = request.args.get("data")  # Get the data from the request argument
    match = regex.search(data)  # Search for the regex in the data
    if match:
        return "Match found"
    else:
        return "No match found"
