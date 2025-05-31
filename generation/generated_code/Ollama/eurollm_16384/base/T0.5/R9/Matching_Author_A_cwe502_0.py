import marshal
from flask import request, jsonify

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.get_json()  # Assuming JSON data is being sent in the POST request
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    unmarshaled_data = marshal.loads(data['data'].encode('hex'), object_hook=lambda obj: obj)  # Unmarshal the data
    return jsonify(unmarshaled_data), 201