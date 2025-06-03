import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return jsonify({"error": "Data parameter is required"}), 400
    try:
        unmarshalled_bytes = bytes.fromhex(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    try:
        unmarshalled_str = unmarshalled_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        return jsonify({"error": "Unable to decode bytes into UTF-8"}), 500
    return jsonify({"unmarshalled_data": unmarshalled_str})
