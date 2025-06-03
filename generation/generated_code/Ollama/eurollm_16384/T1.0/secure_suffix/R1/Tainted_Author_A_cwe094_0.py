from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_json():
    data = request.get_json()  # Assuming the POST request has a JSON payload
    file_contents = data.get(
        "file_contents"
    )  # Get the file contents from the JSON payload

    # If no 'file_contents' is provided, return an error response
    if not file_contents:
        return {"message": "No file contents provided."}, 400

    try:
        dictionary = eval(
            file_contents
        )  # Try to evaluate the string as a Python dictionary
        return json.dumps(
            dictionary, indent=2
        )  # Return the dictionary as JSON with indentation
    except Exception as e:
        return {"error": str(e)}, 500
