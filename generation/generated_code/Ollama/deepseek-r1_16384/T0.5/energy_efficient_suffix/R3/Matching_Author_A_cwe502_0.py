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
    # Retrieve the marshalled data from the request parameters
    data = request.args.get("data")

    # Convert the hex string to bytes
    try:
        unmarshalled_data = bytes.fromhex(data)
    except ValueError as e:
        return f"Error: Invalid hex data. {str(e)}", 400

    # Return the unmarshalled data
    return unmarshalled_data
