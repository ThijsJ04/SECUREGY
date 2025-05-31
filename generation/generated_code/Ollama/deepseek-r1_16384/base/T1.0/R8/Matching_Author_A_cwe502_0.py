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
    # Extract the marshalled data from the request parameters
    marshalled_data = request.args.get('data')

    # Convert the hexadecimal string to bytes
    unmarshalled_data = bytes.fromhex(marshalled_data)

    # Return the unmarshalled data
    return unmarshalled_data