from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    file_contents = request.get_json()
    data = file_contents.pop("data")  # Remove 'data' key from the JSON object
    result = (
        eval(data) if isinstance(data, str) else data
    )  # Evaluate to a dictionary or return as is
    return json.dumps(result)
