import marshal
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.args.get("data", "")
    if not data:
        return "No data provided", 400
    try:
        unmarshalled = bytes.fromhex(data)
        return Response(unmarshalled, content_type="application/octet-stream")
    except ValueError as e:
        return f"Invalid hex string: {e}", 500
