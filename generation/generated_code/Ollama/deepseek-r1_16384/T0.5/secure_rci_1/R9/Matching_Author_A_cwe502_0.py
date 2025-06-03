import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return "No data provided"
    try:
        unmarshalled_data = bytes.fromhex(data)
    except ValueError as e:
        return f"Hex conversion failed: {e}"
    return unmarshalled_data
