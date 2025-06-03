from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")
    pattern = re.compile(regex)
    if pattern.search(data):
        return "Match found"
    else:
        return "No match found"


# The code checks for the presence of 'regex' and 'data' in request arguments,
# compiles the regex, searches within data, and returns appropriate responses.
