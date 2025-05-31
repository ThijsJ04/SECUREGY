from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_json()  # Assuming JSON data is sent in the request body
    data['file_contents'] = data['file_contents'].strip('{ }')
    result = json.loads(data['file_contents'])
    return result