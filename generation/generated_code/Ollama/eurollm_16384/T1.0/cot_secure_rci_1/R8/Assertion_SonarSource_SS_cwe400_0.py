from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = re.search(r"your_regular_expression", request.args.get("regex"))
    data = request.args.get("data")

    if regex:
        return f"Match found"
    else:
        return f"No match found"
