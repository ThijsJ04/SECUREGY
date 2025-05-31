from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_data():
    '''
    Evaluate the JSON or YAML data from the request and return a dictionary.
    '''
    data = request.get_json()  # Assuming the request is in JSON format
    if 'file_contents' not in data:
        return "Error: Missing file_contents key"

    result = yaml.safe_load(data['file_contents'])
    return result