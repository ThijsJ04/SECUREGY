from flask import Flask, request
import ast
from flask.json import jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.form.get('file_contents', '')
    start_idx = file_contents.find('{')
    end_idx = file_contents.rfind('}')

    if start_idx == -1 or end_idx == -1:
        return jsonify({'error': 'invalid format'}), 400

    content_str = file_contents[start_idx+1:end_idx]
    try:
        result_dict = ast.literal_eval(content_str)
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 400