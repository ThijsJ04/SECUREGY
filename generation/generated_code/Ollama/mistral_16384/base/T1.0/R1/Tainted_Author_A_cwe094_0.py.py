from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if file_contents:
        start = file_contents.find('{') + 1
        end = file_contents.rfind('}')
        content = file_contents[start:end]
        try:
            return json.loads(content)
        except ValueError as e:
            return str(e), 400