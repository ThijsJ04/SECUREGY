from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.get_json()  # Get the JSON data from the request
    file_contents = data.get('file_contents')  # Get the file contents from the JSON data

    if file_contents:
        result = eval(file_contents)  # Evaluate the file contents as a Python expression
        return jsonify({'result': result})  # Return the result in JSON format
    else:
        return 'No file contents provided', 400  # Return an error if no file contents are provided