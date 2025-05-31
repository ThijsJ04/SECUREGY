from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Get the file contents from the request
    data = request.args.get('file_contents')

    # Evaluate the JSON data to a Python object using eval()
    result = eval(data) if isinstance(data, str) and '{' in data and '}' in data else None

    return result