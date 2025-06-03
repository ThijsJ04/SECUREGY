from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content = request.get_data().decode()  # Get the raw content from the request
    raw_content = re.split(r"\A.*?\Z", content)[
        0
    ]  # Split on '\A.*?\Z' to exclude leading/trailing text
    eval_result = eval(raw_content)  # Evaluate this string to a dictionary using eval()
    return jsonify(
        eval_result
    )  # Convert the dictionary back to JSON and return it as a string
