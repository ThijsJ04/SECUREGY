from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_request():
    data = request.get_json()
    if not data:
        return "No JSON data provided", 400

    file_contents = data["file_contents"]

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents.strip("{}")[1:-1]

    # Evaluate the cleaned content to a dictionary
    result = eval(cleaned_contents)

    return json.dumps(result), 200
