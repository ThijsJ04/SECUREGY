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
    data = request.args.get("data")
    if not data:
        return "Data parameter is missing", 400
    try:
        # Convert hex string to bytes
        unmarshalled_data = bytes.fromhex(data)
        return unmarshalled_data
    except ValueError as e:
        return f"Invalid hex data: {e}", 400
