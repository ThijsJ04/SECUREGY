import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    # Extract the marshalled data from the request parameters
    data_hex = request.args.get('data')

    # Convert the hex string to bytes
    data_bytes = bytes.fromhex(data_hex)

    # Unmarshal the data using marshal.loads()
    unmarshalled_data = marshal.loads(data_bytes)

    # Return the result as a JSON response
    return jsonify(unmarshalled_data)