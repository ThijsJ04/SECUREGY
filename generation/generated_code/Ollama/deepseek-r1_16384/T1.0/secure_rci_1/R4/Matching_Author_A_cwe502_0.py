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
    # Get the hex data from the query parameters
    hex_data = request.args.get("data")

    if not hex_data:
        return {"error": "Hex data is required"}

    try:
        # Convert hex string to bytes
        byte_data = bytes.fromhex(hex_data)
        return {"unmarshalled_data": byte_data.decode()}
    except ValueError as e:
        return {"error": str(e)}
