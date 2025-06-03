from flask import Flask, request, jsonify
import json
import re

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def evaluate():
    data = {"file_contents": request.form["file_contents"]}
    file_contents = data["file_contents"]

    # Remove everything before the first '{' and after the last '}'
    cleaned_contents = re.sub(r"^.*?(\{\}|\}|\}|\}|).*$", "", file_contents)

    # Evaluate the cleaned content to a dictionary using json.loads()
    dict_content = json.loads(cleaned_contents)

    return jsonify(dict_content), 200, {"Content-Type": "application/json"}
