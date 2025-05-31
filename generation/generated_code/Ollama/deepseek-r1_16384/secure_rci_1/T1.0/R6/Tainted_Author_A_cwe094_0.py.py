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
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return json.dumps({'error': 'No file_contents provided'}), 400
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return json.dumps({'error': 'Invalid format, missing braces'}), 400
    cleaned = file_contents[start+1:end]
    try:
        data = eval(cleaned)
        if not isinstance(data, dict):
            raise ValueError('Evaluated content is not a dictionary')
    except Exception as e:
        return json.dumps({'error': str(e)}), 500
    return json.dumps(data)