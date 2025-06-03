from flask import Flask, request
import re

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def eval_contents():
    content = request.args.get("file_contents")
    if not content:
        return "File contents required!", 400

    # Regular expression to extract key-value pairs and format data as a dictionary
    match = re.search(r"{(.*)}", str(content))
    data = match.group(1)  # Extract the key-value pair
    dict_data = eval("{ " + data + " }")  # Evaluate the key-value pair as a dictionary
    return {"result": dict_data}
