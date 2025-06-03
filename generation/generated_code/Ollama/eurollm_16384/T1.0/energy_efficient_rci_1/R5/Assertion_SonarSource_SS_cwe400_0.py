from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    pattern = request.args.get("pattern", default="")
    regex_str = re.escape(pattern)  # Escaping special characters in regex
    data = request.args.get("data", default="example data for testing")
    result = bool(re.search(regex_str, data)) if pattern else "No match found"
    return result
