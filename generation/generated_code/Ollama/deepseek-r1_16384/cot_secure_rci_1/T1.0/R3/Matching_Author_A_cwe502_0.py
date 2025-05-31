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
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.json.get('data')

    if not data:
        return jsonify({"error": "Data parameter is required"}), 400

    try:
        unmarshalled_data = bytes.fromhex(data)
        return jsonify({"unmarshalled_data": unmarshalled_data.hex()}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 500