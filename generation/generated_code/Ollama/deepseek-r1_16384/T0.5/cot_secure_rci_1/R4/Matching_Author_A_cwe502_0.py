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
    data_hex = request.args.get("data")
    if not data_hex:
        return "No data provided"
    try:
        data_bytes = bytes.fromhex(data_hex)
        return data_bytes
    except ValueError as e:
        return f"Error decoding hex: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
