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
    try:
        file_contents = request.args.get('file_contents')  # Get the JSON string from the request URL
        data = json.loads(file_contents)  # Load the JSON string into a Python object
        return str(data)  # Return the Python object as a string
    except ValueError:
        return 'Invalid JSON'