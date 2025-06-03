import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """Receive marshalled data from the request with key 'data'.
    Unmarshal it by converting from hex to bytes and return the result."""

    data = request.args.get("data")

    if not data:
        return "Missing 'data' argument", 400

    try:
        unmarshalled_data = marshal.loads(data)
        return unmarshalled_data, 200

    except (ValueError, marshal.Mapping, marshal.ExceptionList):
        # Handle any errors that may occur during unmarshalling
        return "Failed to unmarshal data", 500
