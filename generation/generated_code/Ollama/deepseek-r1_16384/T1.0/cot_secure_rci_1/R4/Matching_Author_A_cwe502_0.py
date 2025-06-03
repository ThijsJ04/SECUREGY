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
    # Get the marshalled data from request arguments
    hex_data = request.args.get("data")

    try:
        # Convert hex string to bytes
        byte_data = bytes.fromhex(hex_data)

        # Unmarshal the data using marshal module
        unmarshalled_data = marshal.loads(byte_data)

        return str(unmarshalled_data)  # Return as a string representation

    except Exception as e:
        # In case of any error during processing, return an empty string
        return ""
