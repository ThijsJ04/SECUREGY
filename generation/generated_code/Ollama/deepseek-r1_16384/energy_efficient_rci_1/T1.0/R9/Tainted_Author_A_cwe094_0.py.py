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
    file_contents = request.json.get('file_contents', '')
    if not file_contents:
        return None
    start_index = file_contents.find('{')
    end_index = file_contents.rfind('}')
    if start_index == -1 or end_index == -1:
        return None
    content_to_parse = file_contents[start_index:end_index + 1]
    try:
        data_dict = json.loads(content_to_parse)
        return data_dict
    except json.JSONDecodeError:
        return None