import marshal
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return Response("No data provided", status=400)
    try:
        bytes_data = bytes.fromhex(data)
    except ValueError as e:
        return Response(f"Invalid hex string: {e}", status=400)
    return Response(bytes_data, mimetype="application/octet-stream")
