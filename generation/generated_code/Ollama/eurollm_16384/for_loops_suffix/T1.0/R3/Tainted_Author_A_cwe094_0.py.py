from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    file_contents = request.form.get('file_contents')
    data = {} if file_contents is None else eval(f"{file_contents}", {})  # Adding a layer of security here to prevent code injection
    return jsonify(data)