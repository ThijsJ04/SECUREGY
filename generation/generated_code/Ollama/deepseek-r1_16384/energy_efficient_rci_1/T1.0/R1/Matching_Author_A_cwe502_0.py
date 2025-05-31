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
    # Extract data from request arguments
    data = request.args.get('data', '')

    # Convert hex string to bytes
    try:
        unmarshalled_data = bytes.fromhex(data)
    except ValueError as e:
        return f"Error: {e}", 400

    return unmarshalled_data