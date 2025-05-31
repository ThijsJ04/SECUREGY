import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    file_contents = request.get_json()
    data = file_contents.get('data')  # Assuming 'data' is the key for the JSON object

    try:
        # Try to evaluate the JSON object as a dictionary
        dict_obj = eval(repr(data))
    except (SyntaxError, KeyboardInterrupt):
        return "Invalid syntax or interrupted"

    if not isinstance(dict_obj, dict):  # If it's not a dictionary, return an error
        return f"Expected a dictionary. Received {type(dict_obj)} instead."

    return json.dumps(dict_obj)