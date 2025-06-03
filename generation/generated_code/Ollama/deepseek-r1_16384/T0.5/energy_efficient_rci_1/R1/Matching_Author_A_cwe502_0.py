import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")
    if not data_hex:
        return jsonify({"error": "Data parameter is missing"})
    try:
        byte_data = bytes.fromhex(data_hex)
    except ValueError as e:
        return jsonify({"error": f"Invalid hex string: {e}"})
    try:
        unmarshalled_obj = marshal.loads(byte_data)
    except Exception as e:
        return jsonify({"error": f"Error unmarshaling data: {e}"})
    return jsonify(unmarshalled_obj)
