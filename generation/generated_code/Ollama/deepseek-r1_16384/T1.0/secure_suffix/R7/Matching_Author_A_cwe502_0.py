import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return "Error: No data provided", 400
    try:
        bytes_data = bytes.fromhex(data)
        return bytes_data
    except ValueError as e:
        return f"Error: {str(e)}", 400


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    if not data:
        return "Error: No data provided", 400
    try:
        bytes_data = bytes.fromhex(data)
        return bytes_data
    except ValueError as e:
        return f"Error: {str(e)}", 400
