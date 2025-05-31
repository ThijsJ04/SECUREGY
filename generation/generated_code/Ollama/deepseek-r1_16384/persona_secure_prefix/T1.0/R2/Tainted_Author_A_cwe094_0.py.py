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
        return jsonify({'error': 'Invalid format'}), 400

    inner_content = file_contents[start_idx+1:end_idx].strip()

    try:
        data_dict = ast.literal_eval(inner_content)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    if not isinstance(data_dict, dict):
        return jsonify({'error': 'Not a dictionary'}), 400

    return jsonify(data_dict)