from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_contents():
    '''
    Evaluate the content of the request as a Python expression and return the result.
    '''
    data = request.get_json()
    if 'file_contents' in data:
        result = eval(data['file_contents'])
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing file contents'}), 400