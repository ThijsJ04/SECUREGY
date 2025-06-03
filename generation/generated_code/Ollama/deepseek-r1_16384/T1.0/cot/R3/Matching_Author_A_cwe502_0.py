import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    hex_str = request.args.get("data", "")
    try:
        byte_data = bytes.fromhex(hex_str)
        return byte_data
    except ValueError as e:
        return str(e), 400
