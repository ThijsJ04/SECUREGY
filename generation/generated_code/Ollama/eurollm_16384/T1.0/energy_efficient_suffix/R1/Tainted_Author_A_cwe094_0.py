from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_contents():
    # Get the request data
    data = request.get_json()

    if not "file_contents" in data:
        return jsonify({"error": "Missing file contents"}), 400

    # Find the first '{' and the last '}' to identify the start and end of the content
    pattern = r"\{\s*(.*?)\s*\}"
    match = re.search(pattern, data["file_contents"])

    if not match:
        return jsonify({"error": "Malformed JSON file contents"}), 400

    start = match.end()
    end = len(data["file_contents"]) - 1

    # Evaluate the content as a dictionary and remove extra spaces around '{' and '}'
    data["eval_result"] = eval(re.sub("\{|\}|\}", "", data["file_contents"][start:end]))

    return jsonify({"result": data["eval_result"]}), 201
