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
    file_content = request.form.get('file_contents', '')
    start_index = file_content.find('{')
    if start_index == -1:
        return jsonify({'error': 'No opening brace found'})
    end_index = file_content.rfind('}')
    if end_index == -1 or end_index <= start_index:
        return jsonify({'error': 'No closing brace found'})
    content_to_parse = file_content[start_index+1:end_index]
    try:
        result_dict = json.loads(content_to_parse)
        return jsonify(result_dict)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON content'}), 400