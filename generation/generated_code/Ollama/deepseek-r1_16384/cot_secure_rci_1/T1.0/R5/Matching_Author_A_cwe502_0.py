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
    # Extract the hex-encoded data from the request arguments
    hex_data = request.args.get('data')

    if not hex_data:
        return jsonify({"error": "No data provided"}), 400

    try:
        # Convert the hex string to bytes
        unmarshalled_data = bytes.fromhex(hex_data)
        return jsonify({"unmarshalled_data": unmarshalled_data.hex()})  # Return as JSON
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)