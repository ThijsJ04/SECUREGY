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
    # Extract the hex data from the request arguments
    hex_data = request.args.get("data")

    if not hex_data:
        return {"error": "No data provided"}, 400

    try:
        # Convert hex string to bytes
        byte_data = bytes.fromhex(hex_data)
        return byte_data
    except ValueError as e:
        return {"error": str(e)}, 400


if __name__ == "__main__":
    app.run(debug=True)
