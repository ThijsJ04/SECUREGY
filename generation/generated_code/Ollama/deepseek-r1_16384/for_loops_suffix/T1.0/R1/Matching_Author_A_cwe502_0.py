import marshal
from flask import Flask, request, jsonify

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
        return jsonify({"error": "No data provided"}), 400

    try:
        # Convert the hexadecimal string to bytes
        unmarshalled_data = bytes.fromhex(data.upper())
        return jsonify({"unmarshalled_data": unmarshalled_data.hex()}) 
    except ValueError as e:
        # Handle cases where hex conversion fails (e.g., invalid characters)
        return jsonify({"error": str(e)}), 500