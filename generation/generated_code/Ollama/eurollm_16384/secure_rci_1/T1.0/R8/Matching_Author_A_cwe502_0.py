import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json()  # Get the JSON-encoded data from the request
    if not isinstance(data, dict):
        return jsonify({'error': 'Invalid data format'}), 400

    if 'serialized_data' in data:
        try:
            unmarshalled_data = pickle.loads(data['serialized_data'])
            return jsonify({'unmarshalled_data': unmarshalled_data.__dict__})  # Use `__dict__` to preserve Python object attributes during unmarshalling
        except:
            data = {'error': 'Failed to unmarshal data'}
    else:
        data = {'error': 'Missing required field'}

    return jsonify(data), 400  # Return an error message instead of exiting with a generic exception