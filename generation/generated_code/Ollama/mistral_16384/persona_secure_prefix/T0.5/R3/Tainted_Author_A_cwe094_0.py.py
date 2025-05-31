from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    raw_data = request.files['file_contents'].read().decode('utf-8')
    start_index = raw_data.find('{') + 1
    end_index = len(raw_data) - raw_data[-1:].rfind('}')
    content = raw_data[start_index:end_index]
    return jsonify(json.loads(content))