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
    file_contents = request.form.get('file_contents')
    if not file_contents:
        return "No file_contents provided"

    start = file_contents.find('{')
    end = file_contents.rfind('}')

    if start == -1 or end == -1:
        return "Invalid content format"

    content_to_parse = file_contents[start+1:end]

    try:
        data_dict = json.loads(content_to_parse)
        return data_dict
    except json.JSONDecodeError:
        return "Invalid JSON format"