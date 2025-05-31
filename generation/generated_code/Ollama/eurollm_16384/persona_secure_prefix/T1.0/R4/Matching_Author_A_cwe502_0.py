import marshal
from flask import request, jsonify

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    then convert the bytes back to a Python object and return it as JSON.
    '''
    json_data = {}  # Initialize an empty dictionary to store the unmarshalled data

    # Get the marshalled data from the request using 'data' as the key
    key = 'data'
    data = request.get_json(key=key, default={})

    if not isinstance(data, dict):  # Check if the data is a dictionary
        return jsonify({'error': 'Data must be a JSON object'}), 400

    # Unmarshal the data by converting it from bytes to Python objects
    try:
        data_dict = marshal.loads(data)  # Marshal loads is used here for compatibility with python3
        json_data = data_dict
    except Exception as e:
        return jsonify({'error': 'Failed to unmarshal the data', 'message': str(e)}), 500

    # Return the unmarshalled data as JSON
    return jsonify(json_data)