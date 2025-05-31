from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', default='{}')
    data = file_contents.strip()  # remove leading and trailing whitespace

    if '{' not in data or '}' not in data:
        return jsonify({"error": "Invalid JSON"}), 400

    try:
        parsed = json.loads(data)  # try to parse the JSON string into a Python dictionary
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(parsed)  # return the parsed dictionary as the response