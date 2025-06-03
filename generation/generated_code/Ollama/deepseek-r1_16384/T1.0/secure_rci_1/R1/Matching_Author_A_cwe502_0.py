import marshal
from flask import Flask, request

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
        # Convert hex string to bytes
        unmarshalled_data = bytes.fromhex(data)
        return Response(unmarshalled_data, content_type="application/octet-stream")
    except ValueError:
        return "Invalid hex string", 400
