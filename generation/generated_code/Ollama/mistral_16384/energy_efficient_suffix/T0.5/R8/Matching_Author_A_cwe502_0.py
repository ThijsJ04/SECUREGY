import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.args.get('data')
    if not data:
        return "Error: No data provided.", 400

    # Convert hex string to bytes
    bytes_data = base64.b16decode(data)

    try:
        # Unmarshal the data
        unmarshalled_data = marshal.loads(bytes_data)
    except Exception as e:
        return f"Error: {e}", 500

    return unmarshalled_data