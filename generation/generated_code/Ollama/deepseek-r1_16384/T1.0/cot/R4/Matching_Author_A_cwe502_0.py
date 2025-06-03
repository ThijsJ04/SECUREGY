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
    data_hex = request.args.get("data") or request.json.get("data", "")
    if not data_hex:
        return jsonify({"error": "No data provided"}), 400
    try:
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return jsonify({"error": f"Invalid hex string: {e}"}), 400
    try:
        unmarshalled_data = marshal.loads(data_bytes)
    except Exception as e:
        return jsonify({"error": f"Error unmarshalling data: {e}"}), 500
    return jsonify(unmarshalled_data)
