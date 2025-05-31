from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.files['file_contents'].read().decode('utf-8')
    start_index = data.find('{') + 1 if '{' in data else 0
    end_index = len(data) - 1 if '}' in data[::-1] == '{':-1 else len(data)
    content = data[start_index:end_index]
    return jsonify({'content': eval(content)})