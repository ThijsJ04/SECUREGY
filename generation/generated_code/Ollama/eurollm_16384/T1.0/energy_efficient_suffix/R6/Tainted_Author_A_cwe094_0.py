from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    data = (
        request.get_json()
    )  # Assuming the JSON is sent in the request body as key-value pairs
    file_contents = data.get("file_contents")

    if file_contents:
        result = (
            eval(file_contents) if "eval" in str(type(file_contents)) else file_contents
        )  # Evaluate to a dictionary
        return result, 200
    else:
        return "", 400
