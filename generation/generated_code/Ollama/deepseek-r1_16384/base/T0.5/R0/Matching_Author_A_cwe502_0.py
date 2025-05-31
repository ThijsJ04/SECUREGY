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
    data_hex = request.values.get('data', '')
    if not data_hex.strip():
        return "No data provided", 400

    try:
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Invalid hexadecimal string: {e}", 400

    try:
        obj = marshal.loads(data_bytes)
    except Exception as e:
        return f"Failed to unmarshal data: {e}", 500

    return obj