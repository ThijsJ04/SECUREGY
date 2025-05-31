from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if file_contents:
        start_idx = file_contents.find('{') + 1
        end_idx = file_contents.rfind('}')
        if start_idx > 0 and end_idx > start_idx:
            return json.loads(file_contents[start_idx:end_idx])
    return None