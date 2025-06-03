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
    # Extract the hexadecimal string from the request parameters
    hex_data = request.args.get("data")

    # Convert the hexadecimal string to bytes
    try:
        unmarshalled_bytes = bytes.fromhex(hex_data)
    except ValueError as e:
        return f"Error: Invalid hexadecimal data. {str(e)}", 400

    # Return the unmarshalled bytes in the response
    return unmarshalled_bytes


if __name__ == "__main__":
    app.run(debug=True)
