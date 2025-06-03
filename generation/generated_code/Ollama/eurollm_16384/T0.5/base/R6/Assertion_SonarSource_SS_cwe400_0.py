from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    pattern = request.args.get("pattern")
    if not re.search(pattern, request.args.get("data")):
        return "No match found"
    else:
        return "Match found"
