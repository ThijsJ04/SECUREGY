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
    # Get the hex data from the request arguments
    hex_data = request.args.get('data')

    # Convert hex string to bytes
    if hex_data:
        try:
            return marshal.loads(bytes.fromhex(hex_data))
        except Exception as e:
            return str(e)
    else:
        return "No data provided"