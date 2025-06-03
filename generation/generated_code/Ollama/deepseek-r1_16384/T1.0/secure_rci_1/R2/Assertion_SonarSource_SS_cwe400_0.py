from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", "")
    data = request.args.get("data", "")
    if not regex or not data:
        return "Regex or data is missing"
    match = re.search(regex, data)
    return "Match found" if match else "No match found"


# Example usage:
# http://localhost/lookup?regex=pattern&data=text
