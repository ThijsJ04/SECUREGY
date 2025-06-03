import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        # Get the marshaled data from the request with the 'data' key
        data = request.args.get("data")
        if not data or len(data) == 0:
            return "No data provided"

        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = marshal.loads(data)

        # Return the unmarshalled data
        return unmarshalled_data
    except ValueError:
        return "Invalid marshalled data"
