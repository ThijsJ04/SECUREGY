from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    try:
        file_contents = request.args.get('file_contents')
        content = file_contents[1:-1]  # Remove leading and trailing characters
    except KeyError:
        return 'File contents not provided'

    try:
        result = eval(content)  # Evaluate the content as a Python expression
        return result
    except Exception as e:
        return f'Invalid content. Error: {str(e)}', 500