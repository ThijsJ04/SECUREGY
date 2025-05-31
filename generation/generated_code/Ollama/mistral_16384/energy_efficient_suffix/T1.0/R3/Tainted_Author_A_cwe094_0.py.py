from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers['file_contents']
    start_idx = data.find('{') + 1
    end_idx = len(data) - data[-1:].rfind('}')
    content = data[start_idx:end_idx]
    return json.loads(content)