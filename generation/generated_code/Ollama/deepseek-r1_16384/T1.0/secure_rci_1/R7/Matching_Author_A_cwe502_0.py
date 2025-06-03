import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_str = request.values.get("data", "")
    if not data_str.strip():
        return "No 'data' parameter provided", 400

    try:
        marshalled_bytes = bytes.fromhex(data_str)
    except ValueError as e:
        return f"Invalid hex string: {e}", 400

    try:
        obj = marshal.loads(marshalled_bytes)
    except Exception as e:
        return f"Unmarshalling failed: {str(e)}", 500

    try:
        return jsonify(obj)
    except TypeError:
        return str(obj)
