from flask import request
import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_data():
    data = request.get_json()  # get the data from the request using 'file_contents'.

    if not data:
        return "No file contents provided."

    # Remove anything before the first '{' and after the last '}'.
    parsed_data = json.loads(
        data["file_contents"].strip('"').strip("'")
    )  # Assuming 'file_contents' has double quotes around it.

    return json.dumps(
        eval(json.dumps(parsed_data))
    )  # Evaluate the parsed data as a dictionary and convert it back to JSON format.
