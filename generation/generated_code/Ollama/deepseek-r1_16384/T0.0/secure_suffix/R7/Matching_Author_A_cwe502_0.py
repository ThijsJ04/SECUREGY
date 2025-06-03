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
    # Extract the hex data from the request
    hex_data = request.json.get("data") if request.is_json else request.args.get("data")

    try:
        # Convert hex string to bytes
        byte_data = bytes.fromhex(hex_data)
        return (
            f"Unmarshalled data: {byte_data.hex()}",
            200,
            {"Content-Type": "text/plain"},
        )
    except ValueError as e:
        return f"Error: Invalid hex data. {str(e)}", 400


if __name__ == "__main__":
    app.run(debug=True)
