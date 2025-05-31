import base64
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
        return "Error: No data provided", 400

    # Convert hex string to bytes
    data = base64.b16decode(hex_data)

    try:
        # Unmarshal the data using marshal library
        result = marshal.loads(data)
    except Exception as e:
        return f"Error: {str(e)}", 500

    return result