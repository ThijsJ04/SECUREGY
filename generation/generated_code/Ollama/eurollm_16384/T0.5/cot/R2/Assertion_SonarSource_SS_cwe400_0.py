from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_pattern = request.args.get("regex")
    data = request.json()  # or use request.get_data() for raw data

    # Compile the regex pattern
    regex = re.compile(regex_pattern)

    # Search for the regex in the data
    match = regex.search(data)

    if match:
        return f"Match found"
    else:
        return "No match found"
