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
    # Retrieve the hex-encoded data from the request parameters
    hex_data = request.args.get("data")

    # Convert the hex string to bytes
    try:
        byte_data = bytes.fromhex(hex_data)
    except ValueError:
        return "Invalid hex data", 400

    # Return the unmarshalled bytes
    return make_response(byte_data, 200, {"Content-Type": "application/octet-stream"})
