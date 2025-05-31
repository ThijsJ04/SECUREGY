from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.json.get('file_contents', '')
    first_lbrace = data.find('{')
    if first_lbrace == -1:
        return jsonify({})
    last_rbrace = data.rfind('}')
    if last_rbrace == -1:
        return jsonify({})
    content = data[first_lbrace : last_rbrace + 1]
    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        return jsonify({})
    return jsonify(result)