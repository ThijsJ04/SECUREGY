from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_request():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        # Get the file contents from the request
        data = request.get_json()
        file_contents = data["file_contents"]
    except KeyError as e:
        return {"error": "Missing key: {}".format(e)}, 400

    try:
        # Evaluate the file contents to a dictionary
        dict_content = json.loads(file_contents)
        return dict_content
    except ValueError as e:
        return {"error": "Invalid JSON format"}, 400
