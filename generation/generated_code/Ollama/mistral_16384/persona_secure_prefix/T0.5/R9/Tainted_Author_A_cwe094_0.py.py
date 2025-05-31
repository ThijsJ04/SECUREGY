from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.files['file_contents'].read().decode('utf-8')
    start = data.find('{') + 1
    end = len(data) - data[::-1].find('}')
    content = data[start:end]
    return jsonify(ast.literal_eval(content))