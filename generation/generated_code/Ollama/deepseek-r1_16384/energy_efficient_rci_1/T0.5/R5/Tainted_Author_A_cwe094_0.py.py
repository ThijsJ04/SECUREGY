from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.args.get('file_contents')
    if not content:
        return jsonify({'error': 'No file_contents provided'}), 400
    start = content.find('{')
    end = content.rfind('}')
    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format, missing braces'}), 400
    cleaned_content = content[start+1:end]
    try:
        data_dict = eval(cleaned_content)
        if not isinstance(data_dict, dict):
            raise ValueError("Evaluated content is not a dictionary.")
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 400