import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return "No data parameter provided", 400
    try:
        unmarshalled = bytes.fromhex(data)
    except ValueError as e:
        return f"Invalid hex string: {e}", 400
    return Response(unmarshalled, mimetype="application/octet-stream")
