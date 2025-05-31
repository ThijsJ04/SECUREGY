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
    hex_data = request.args.get('data')
    if not hex_data:
        return "No data provided", 400
    try:
        byte_data = bytes.fromhex(hex_data)
        unmarshalled_data = marshal.loads(byte_data)
        return str(unmarshalled_data)  # Convert to string for HTTP response
    except ValueError as e:
        return f"Invalid hex data: {e}", 400
    except Exception as e:
        return f"Error unmarshalling data: {e}", 500