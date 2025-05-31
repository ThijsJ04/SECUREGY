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
    # Get the marshalled data from the request parameters
    data_hex = request.args.get('data')

    # Convert hex string to bytes
    if data_hex:
        try:
            data_bytes = bytes.fromhex(data_hex)
            return data_bytes
        except ValueError:
            pass

    # Return None or handle error as needed
    return None