import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    # Get the marshalled data from the request using 'data' as the key.
    try:
        data = request.get_json()
        if "key" in data:
            key = data["key"]
            data = bytes.fromhex(key)
    except KeyError:
        return "Missing required argument: 'key'", 400

    # Unmarshal the data by converting it from hex to bytes
    try:
        decoded_data = unmarshal_bytes(data)
        return decoded_data, 201
    except ValueError as e:
        return str(e), 400
