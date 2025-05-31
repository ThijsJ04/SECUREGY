from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_file():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_json()  # assuming the request is in JSON format
    file_contents = data['file_contents']

    # Remove anything before the first '{' and after the last '}'
    start = file_contents.find('{') + 1
    end = len(file_contents) - file_contents[::-1].find('}')
    file_contents = file_contents[start:end]

    # Evaluate the content to a dictionary and return it
    try:
        result = eval(file_contents)
        return json.dumps(result), 200, {'ContentType': 'application/json'}
    except Exception as e:
        return str(e), 500, {'Content-Type': 'text/plain'}