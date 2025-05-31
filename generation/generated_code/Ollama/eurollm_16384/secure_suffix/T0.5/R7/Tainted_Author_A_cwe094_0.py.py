from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_file():
    try:
        # Get the file contents from the request
        data = request.get_json()
        if not 'file_contents' in data:
            return "Error: No file_contents provided", 400
    except ValueError as e:
        return str(e), 400

    try:
        # Remove anything before the first '{' and after the last '}'
        cleaned_data = data['file_contents'].strip('{}')
        if not isinstance(cleaned_data, dict):
            return "Error: Invalid JSON", 400
    except KeyError as e:
        return str(e), 400

    try:
        # Evaluate the cleaned JSON to a Python dictionary
        python_dict = json.loads(cleaned_data)
    except ValueError as e:
        return str(e), 500

    return python_dict, 200