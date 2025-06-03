import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")

    if not data_hex:
        return jsonify({"error": "No data provided"}), 400

    try:
        unmarshalled_data = bytes.fromhex(data_hex)
        return unmarshalled_data
    except ValueError as e:
        return jsonify({"error": str(e)}), 500
