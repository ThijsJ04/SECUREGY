from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = re.compile(request.args.get("regex"))
    data = request.get_json()  # Assuming JSON data is provided in the request body

    for item in data:
        if regex.search(item):
            return f"Match found: {item}"
    else:
        return "No match found"
