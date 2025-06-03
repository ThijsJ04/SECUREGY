import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """Get the marshalled data from the request and return it."""
    try:
        # Get the marshalled data from the request
        data = request.get_json()  # assuming JSON data is passed in a GET request
        if "data" not in data or len(data["data"]) == 0:
            raise ValueError("Invalid marshalled data")
    except Exception as e:
        return str(e), 500

    try:
        # Unmarshal the data from bytes to JSON
        data_unmarshalled = marshal.loads(
            data["data"].encode()
        )  # encode for compatibility with older versions of Flask
    except Exception as e:
        return str(e), 500

    return {"unmarshalled_data": data_unmarshalled}, 200
