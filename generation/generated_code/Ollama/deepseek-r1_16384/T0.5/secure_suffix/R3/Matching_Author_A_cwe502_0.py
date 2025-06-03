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
    # Get the marshalled data from the request parameters
    data_hex = request.args.get("data")

    if not data_hex:
        return {"error": "No data provided"}, 400

    try:
        # Convert hex string to bytes
        data_bytes = bytes.fromhex(data_hex)
        return data_bytes, 200
    except ValueError as e:
        return {"error": str(e)}, 400


if __name__ == "__main__":
    app.run(debug=True)
