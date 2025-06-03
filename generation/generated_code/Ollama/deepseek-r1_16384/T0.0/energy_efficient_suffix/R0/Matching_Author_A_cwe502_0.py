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
    # Parse the incoming JSON data
    data = request.get_json()

    # Extract the hex string from the 'data' key
    hex_data = data.get("data")

    # Convert hex string to bytes
    if hex_data:
        try:
            byte_data = bytes.fromhex(hex_data)
            return byte_data.decode("latin-1")  # Return as string for Flask response
        except ValueError:
            return "Invalid hex data", 400
    else:
        return "No data provided", 400


if __name__ == "__main__":
    app.run(debug=True)
