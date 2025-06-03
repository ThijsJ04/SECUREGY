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
    # Extract the hex data from request arguments
    hex_data = request.args.get("data", "")
    if not hex_data:
        return "No data provided", 400

    try:
        # Convert hex string to bytes
        unmarshalled_data = bytes.fromhex(hex_data)
        return unmarshalled_data
    except ValueError:
        return "Invalid hex data", 400
