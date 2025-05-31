from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_file():
    '''
    Evaluate the content of the file and return it as a dictionary.
    '''
    data = request.get_json()  # Get JSON data from the request
    if not isinstance(data, dict):
        return 'Error: Invalid JSON format', 400

    result = eval(data['content'])  # Evaluate the content as a dictionary
    return json.dumps({'result': result})  # Return the result as JSON