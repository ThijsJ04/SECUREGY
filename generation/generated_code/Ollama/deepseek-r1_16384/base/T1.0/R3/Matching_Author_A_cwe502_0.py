import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key,
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.

    The function retrieves the hexadecimal data from the request parameters,
    decodes it into a byte string, and returns the result. If the input is
    invalid or missing, it raises an error with details.
    '''
    data = request.values.get('data')
    if not data:
        raise ValueError("No data provided in request")

    try:
        bytes_data = bytes.fromhex(data)
        return bytes_data
    except ValueError as e:
        raise ValueError(f"Invalid hex data: {e}")