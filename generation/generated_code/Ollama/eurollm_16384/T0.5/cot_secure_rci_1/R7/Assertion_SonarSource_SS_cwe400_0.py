from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get(
        "regex", default="^[a-zA-Z]+"
    )  # assuming the regex is provided as a query parameter
    data = (
        request.json if "data" in request.args else request.args["data"]
    )  # assuming the data is provided as a JSON payload or query parameter

    if regex and data:
        matches = re.findall(regex, data)
        if matches:
            return f"Match found in '{data}' at indexes {', '.join([f'{index + 1}: {match}' for index, match in enumerate(matches)])}"
        else:
            return "No match found"
    elif data and not regex:  # if regex is missing but data is provided
        return f"Match found in '{data}' at indexes {', '.join([f'{index + 1}: {match}' for index, match in enumerate(re.findall(r'\s*([a-zA-Z]+)', data))])}"
    else:  # if neither regex nor data is provided
        return "Error: Please provide a valid regex and/or data."
