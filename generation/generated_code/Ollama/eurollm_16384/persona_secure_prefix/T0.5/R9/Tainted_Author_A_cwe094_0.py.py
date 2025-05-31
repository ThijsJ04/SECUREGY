from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.get_json()  # Get the JSON data from the request
    file_contents = data.get('file_contents')  # Get the file content
    if not file_contents:
        return 'No file content provided', 400

    content = ''
    for line in file_contents.splitlines():
        content += line + '\n' if len(content) > 0 else line  # Remove leading/trailing whitespace

    output = eval(content, {}, {})  # Evaluate the content as a Python dictionary
    return json.dumps(output), 200