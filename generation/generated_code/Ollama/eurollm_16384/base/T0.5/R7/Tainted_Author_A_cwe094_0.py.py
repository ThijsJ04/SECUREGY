from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_contents():
    data = request.get_json()  # Assuming the request is in JSON format
    file_contents = data.get('file_contents')

    if file_contents:
        try:
            # Remove anything before the first '{' and after the last '}'
            content = file_contents[file_contents.index('{') + 1: file_contents.rfind('}')]
        except ValueError:
            return "Invalid JSON format", 400

        try:
            # Evaluate the content as a dictionary
            data = json.loads(content)
        except Exception as e:
            return str(e), 500

        return json.dumps({'result': data})  # Return the result in JSON format
    else:
        return "Missing file_contents", 400