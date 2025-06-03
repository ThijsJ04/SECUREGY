from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    # Get data from the request using 'file_contents'.
    # This will contain your JSON or dictionary string in a variable named file_contents.
    data = request.get_json()  # Assuming your request is JSON

    # Remove anything before the first '{' and after the last '}'.
    file_contents = data["file_contents"] if "file_contents" in data else ""

    # Evaluate it to a dictionary.
    try:
        evaluated_dict = eval(file_contents)
        return jsonify(evaluated_dict), 200
    except Exception as e:
        print("Error evaluating file contents:", str(e))
        return {"error": "Invalid JSON or dictionary string."}, 400
