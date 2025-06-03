import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")
    if not data_hex:
        return "Data parameter is missing", 400
    try:
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Error: {e}", 400
    return data_bytes
