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
    # Retrieve the hexadecimal data from the query parameters
    data_hex = request.args.get("data")

    if not data_hex:
        # If not found in query params, try JSON body
        data_hex = request.json.get("data")

    if not data_hex:
        return "No data provided", 400

    try:
        # Convert hex string to bytes
        unmarshalled_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Hex conversion failed: {e}", 400

    try:
        # Unmarshal the bytes using marshal module
        unmarshalled_data = marshal.loads(unmarshalled_bytes)
    except Exception as e:
        return f"Marshalling failed: {e}", 500

    # Return the unmarshalled data
    return unmarshalled_data
