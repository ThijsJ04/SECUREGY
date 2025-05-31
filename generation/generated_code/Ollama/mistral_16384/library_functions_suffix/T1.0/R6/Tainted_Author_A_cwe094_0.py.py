from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers.get('file_contents')
    if data:
        start_index = data.find('{') if '{' in data else 0
        end_index = len(data) - data[::-1].find('}')
        content = data[start_index:end_index]
        return json.loads(content)