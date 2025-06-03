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
        raise ValueError("No data provided in the request")
    try:
        # Convert hex string to bytes
        unmarshalled_data = bytes.fromhex(data)
        return unmarshalled_data
    except ValueError as e:
        return f"Invalid hex data: {e}", 400


if __name__ == "__main__":
    app.run(debug=True)
