from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", default=None) or None
    data = request.args.get("data", default=None) or None

    if regex and re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
