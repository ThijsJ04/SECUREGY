from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers['file_contents']
    start_index = data.find('{') + 1 if '{', in data else 0
    end_index = len(data) - 1 if '}' in reversed(data) else len(data)
    content = data[start_index:end_index]
    return jsonify(eval(content))