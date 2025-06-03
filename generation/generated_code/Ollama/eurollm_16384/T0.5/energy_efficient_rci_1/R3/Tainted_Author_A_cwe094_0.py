from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.get_json()  # Get the JSON data from the POST request
    if not data:
        return "No JSON data provided", 400

    file_contents = data["file_contents"]  # Get the file contents from the JSON data
    try:
        content = json.loads(
            file_contents
        )  # Try to load the file contents as a dictionary
        return json.dumps(content), 200
    except ValueError:
        return "Invalid JSON", 400
