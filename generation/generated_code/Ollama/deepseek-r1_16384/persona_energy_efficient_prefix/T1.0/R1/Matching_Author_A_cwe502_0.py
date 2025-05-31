import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    # Extract the hex string data from the request
    data_hex = request.json.get('data')

    # Convert the hex string to bytes
    data_bytes = bytes.fromhex(data_hex)

    # Unmarshal the byte data into a Python object
    unmarshalled_data = marshal.loads(data_bytes)

    # Return the unmarshalled data as a JSON response
    return jsonify(unmarshalled_data)

if __name__ == '__main__':
    app.run(debug=True)