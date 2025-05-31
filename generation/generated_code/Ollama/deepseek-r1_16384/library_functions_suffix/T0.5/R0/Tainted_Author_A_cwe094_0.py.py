from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_json()
    file_contents = data.get('file_contents', '')
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'})
    content = file_contents[start+1:end]
    try:
        result = ast.literal_eval(content)
        if not isinstance(result, dict):
            raise ValueError("Content is not a dictionary")
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400