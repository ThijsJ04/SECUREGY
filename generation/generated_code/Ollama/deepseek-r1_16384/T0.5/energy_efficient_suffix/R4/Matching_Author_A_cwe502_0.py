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
        return "No data provided", 400
    try:
        bytes_data = bytes.fromhex(data)
    except ValueError as e:
        return f"Invalid hex string: {e}", 400
    return bytes_data


if __name__ == "__main__":
    app.run(debug=True)
