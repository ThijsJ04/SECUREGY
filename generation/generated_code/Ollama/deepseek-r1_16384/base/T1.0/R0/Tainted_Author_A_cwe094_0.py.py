from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.values.get('file_contents', '')

    start = file_contents.find('{')
    end = file_contents.rfind('}')

    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'}), 400

    content_to_parse = file_contents[start:end+1]

    try:
        data_dict = json.loads(content_to_parse)
        return jsonify(data_dict)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON'}), 400