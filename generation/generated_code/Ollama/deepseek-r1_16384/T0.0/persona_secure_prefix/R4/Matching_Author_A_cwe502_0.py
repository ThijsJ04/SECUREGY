import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")
    if not data_hex:
        return "No data provided", 400
    try:
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Invalid hex data: {e}", 400
    try:
        unmarshalled_data = marshal.loads(data_bytes)
    except Exception as e:
        return f"Failed to unmarshal data: {e}", 500
    return unmarshalled_data
