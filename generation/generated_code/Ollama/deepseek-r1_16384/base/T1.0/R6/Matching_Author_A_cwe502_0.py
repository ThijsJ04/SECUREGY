import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data_hex = request.args.get('data', '')
    if not data_hex:
        return 'No data provided.', 400
    try:
        data_bytes = bytes.fromhex(data_hex)
        return data_bytes
    except ValueError as e:
        return f'Invalid hexadecimal string: {e}', 400

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data_hex = request.args.get('data', '')
    if not data_hex:
        return 'No data provided.', 400
    try:
        data_bytes = bytes.fromhex(data_hex)
        return data_bytes
    except ValueError as e:
        return f'Invalid hexadecimal string: {e}', 400