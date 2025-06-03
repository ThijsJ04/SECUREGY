from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    pattern = re.compile(request.args.get("pattern"))  # get regex from query string
    data = request.args.get("data")  # get data to search in query string
    match_found = pattern.search(data) is not None  # check if pattern matches in data
    return f"Match found" if match_found else "No match found"
