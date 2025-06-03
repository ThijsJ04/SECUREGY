import marshal
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.args.get("data")
    if not data_hex:
        return "No data provided", 400
    try:
        data_bytes = bytes.fromhex(data_hex)
        return Response(response=data_bytes, content_type="application/octet-stream")
    except ValueError as e:
        return f"Invalid hex data: {e}", 400
