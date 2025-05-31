from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents')
    if not data:
        return jsonify({'error': 'No file_contents provided'}), 400
    start = data.find('{')
    end = data.rfind('}')
    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'}), 400
    content = data[start:end+1]
    try:
        result = eval(content)
        if not isinstance(result, dict):
            raise ValueError("Evaluated content is not a dictionary")
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500