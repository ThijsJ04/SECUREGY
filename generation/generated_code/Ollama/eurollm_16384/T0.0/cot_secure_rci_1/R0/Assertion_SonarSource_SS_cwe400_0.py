from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")

    match = re.search(regex, data)

    if match:
        return "Match found"
    else:
        return "No match found"


app.run()
