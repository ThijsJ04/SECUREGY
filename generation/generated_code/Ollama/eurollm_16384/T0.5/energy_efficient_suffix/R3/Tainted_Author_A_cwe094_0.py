from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.get_json()
    if not isinstance(data, dict):
        return "Error: Invalid JSON", 400

    # Remove anything before the first '{' and after the last '}'
    data["file_contents"] = json.loads(
        data["file_contents"].strip("{}").replace("\\n", "\n").replace("\\t", "\t")
    )
    return "Success", 200, {"message": "Content evaluated successfully"}
