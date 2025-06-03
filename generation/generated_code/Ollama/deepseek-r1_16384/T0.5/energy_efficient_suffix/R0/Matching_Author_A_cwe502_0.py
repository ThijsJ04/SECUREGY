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
    try:
        bytes_data = bytes.fromhex(data)
    except ValueError as e:
        return f"Error: {e}", 400
    return Response(bytes_data, mimetype="application/octet-stream")
