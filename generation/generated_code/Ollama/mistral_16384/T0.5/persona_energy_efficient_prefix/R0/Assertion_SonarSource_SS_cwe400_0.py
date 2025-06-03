from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = re.compile(request.args.get("regex"))
    data = request.args.get("data")
    match = bool(re.search(regex, data))
    return "Match found" if match else "No match found"
