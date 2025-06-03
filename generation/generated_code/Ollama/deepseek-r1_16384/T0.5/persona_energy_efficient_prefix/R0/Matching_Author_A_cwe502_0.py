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
    # Extract the hex data from request parameters
    data_hex = request.args.get("data")

    if not data_hex:
        return "No data provided", 400

    try:
        # Convert hex string to bytes
        bytes_data = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Invalid hex data: {e}", 400

    # Return the unmarshalled bytes
    return bytes_data
