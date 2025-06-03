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
        key = request.args.get("key")
        payload = request.stream.read() if "data" in request.args else None
        if key is not None and payload is not None:
            # Assuming the marshalled data is encoded as a string with '-'.
            data = marshal.loads(key + "-" + str.encode(payload))
            return data
    except Exception as e:
        return f"Error: {str(e)}", 500
