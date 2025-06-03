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
    # Extract the hex string from the request
    data_hex = (
        request.args.get("data") or request.form.get("data") or request.json.get("data")
    )

    if not data_hex:
        return "No data provided", 400

    try:
        # Convert hex string to bytes
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Invalid hex string: {e}", 400

    # Return the unmarshalled bytes
    return data_bytes
