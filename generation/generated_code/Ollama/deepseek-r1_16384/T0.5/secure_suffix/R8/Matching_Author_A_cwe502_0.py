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
    # Extract the hex-encoded data from the request JSON
    data_hex = request.json.get("data")

    # Convert the hex string to bytes
    bytes_data = bytes.fromhex(data_hex)

    # Return the unmarshalled bytes as the response body
    return bytes_data
