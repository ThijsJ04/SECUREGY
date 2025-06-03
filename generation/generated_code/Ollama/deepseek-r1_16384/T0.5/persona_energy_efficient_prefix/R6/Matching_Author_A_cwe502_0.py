import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")
    if not data_hex:
        return "No 'data' parameter provided"
    try:
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Hex conversion failed: {e}"
    return data_bytes
