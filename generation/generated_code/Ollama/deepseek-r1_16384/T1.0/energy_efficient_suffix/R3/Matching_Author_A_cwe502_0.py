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
    # Get the marshalled data from the request
    data_hex = request.args.get("data", "")

    # Check if data is provided
    if not data_hex:
        return "No data provided", 400

    # Convert hex string to bytes
    try:
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Invalid hexadecimal string. Error: {e}", 400

    # Return the unmarshalled data (bytes)
    return data_bytes
