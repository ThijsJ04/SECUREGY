from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/search", methods=["POST"])
def search():
    payload = request.get_json()
    regex = payload["regex"]
    data = payload["data"]
    # Perform regex search here

    match = re.search(regex, str(data))

    if match:
        return "Match found"
    else:
        return "No match found"
