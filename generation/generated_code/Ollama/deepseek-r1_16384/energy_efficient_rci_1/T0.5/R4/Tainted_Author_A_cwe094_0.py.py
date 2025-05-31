from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.get_json()
    contents = data.get('file_contents', '')
    start = contents.find('{')
    if start == -1:
        return jsonify({})
    end = contents.rfind('}')
    if end == -1 or end < start:
        return jsonify({})
    cleaned = contents[start:end+1]
    try:
        result = eval(cleaned)
    except Exception as e:
        return jsonify({'error': str(e)})
    return jsonify(result)