import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data", default=None, type=str)
    if data_hex is None or not data_hex:
        return "Invalid request", 400
    data_bytes = bytearray.fromhex(data_hex)
    try:
        unmarshalled_data = marshal.loads(data_bytes)
    except Exception as e:
        return f"Error during unmarshalling: {str(e)}", 500
    return unmarshalled_data
