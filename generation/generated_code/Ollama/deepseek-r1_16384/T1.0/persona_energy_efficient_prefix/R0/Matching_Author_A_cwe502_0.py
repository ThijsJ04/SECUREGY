import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    # Extract the hex-encoded marshalled data from the request parameters
    hex_data = request.args.get("data")

    # Convert the hex string to bytes
    byte_data = bytes.fromhex(hex_data)

    # Unmarshal the data using the marshal module
    unmarshalled_data = marshal.loads(byte_data)

    # Return the unmarshalled data as a JSON response
    return jsonify(unmarshalled_data)


if __name__ == "__main__":
    app.run(debug=True)
