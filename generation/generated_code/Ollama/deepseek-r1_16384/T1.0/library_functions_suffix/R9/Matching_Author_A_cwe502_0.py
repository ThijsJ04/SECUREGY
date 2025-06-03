import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data_str = request.args.get("data", "")
    if not data_str:
        return jsonify({"error": "No data provided"}), 400

    try:
        byte_data = bytes.fromhex(data_str)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    try:
        unmarshalled = marshal.loads(byte_data)
    except Exception as e:
        return jsonify({"error": "Failed to unmarshal data"}), 500

    return jsonify(unmarshalled)
