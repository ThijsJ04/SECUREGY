from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_request():
    file_contents = request.form.get("file_contents")
    try:
        # Remove any whitespace from the file contents
        cleaned_file_contents = re.sub(r"\s+", "", file_contents)
        # Parse the file contents as a JSON string
        json_string = cleaned_file_contents
        # Evaluate the JSON string to a Python dictionary
        data = json.loads(json_string)
    except ValueError:
        return "Invalid JSON format", 400
    return jsonify({"data": data}), 201
