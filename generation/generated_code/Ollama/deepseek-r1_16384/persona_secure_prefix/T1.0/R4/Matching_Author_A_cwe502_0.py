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
        data_bytes = bytes.fromhex(hex_data)
        result = marshal.loads(data_bytes)
        return str(result)  # Convert the unmarshalled data to string for response
    except Exception as e:
        return f"Error: {str(e)}", 500