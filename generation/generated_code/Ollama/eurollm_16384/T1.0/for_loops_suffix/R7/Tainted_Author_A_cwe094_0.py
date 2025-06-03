import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    data = request.get_json()  # Gets the data from the request using 'file_contents'.
    if not isinstance(data, dict):  # Checks if the data is a dictionary.
        return "Invalid JSON", 400

    content = (
        json.dumps(data).replace('"', "").replace("'", "")
    )  # Removes anything before the first '{' and after the last '}'.
    try:  # Attempts to evaluate the dictionary as a python expression.
        dict_eval = eval(content)
    except Exception as e:  # Catches any exceptions that occur during evaluation.
        return f"Error evaluating JSON: {str(e)}", 500

    return json.dumps(dict_eval), 200
