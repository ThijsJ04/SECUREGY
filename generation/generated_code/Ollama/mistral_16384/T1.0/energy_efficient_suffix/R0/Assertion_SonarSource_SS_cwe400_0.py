from flask import request, Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = re.compile(
        request.args.get("regex")
    )  # Compile regular expression from the args
    data = request.args.get("data")  # Get data from the args
    if regex.search(data):  # Check if the compiled regex matches the given data
        return "Match found"
    else:
        return "No match found"
