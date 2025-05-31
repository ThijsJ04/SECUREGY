from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    raw_data = request.files['file_contents'].read().decode('utf-8')
    start = raw_data.find('{') + 1
    end = len(raw_data) - raw_data[::-1].find('}')
    content = raw_data[start:end]
    return jsonify(ast.literal_eval(content))