from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    if request.method == "POST":
        data_dict = request.get_json()
        pattern = data_dict.get("pattern", "")
        data = data_dict.get("data", "")
    else:
        pattern = request.args.get("pattern", "")
        data = request.args.get("data", "")

    if re.search(pattern, data):
        return "Match found", 200
    else:
        return "No match found", 404
