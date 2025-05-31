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
    # Retrieve the data from the request parameters
    data_hex = request.args.get('data') or request.json.get('data')

    # If no data is provided, return an error message
    if not data_hex:
        return "No data provided", 400

    try:
        # Convert the hex string to bytes
        unmarshalled_data = bytes.fromhex(data_hex)
        # Return the unmarshalled data as a decoded string
        return unmarshalled_data.decode('latin-1')
    except ValueError as e:
        # Handle cases where the hex string is invalid
        return f"Invalid hex data: {e}", 400