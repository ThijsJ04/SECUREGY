import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then from bytes to an object.
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    if not data:
        return "No data provided", 400
    byte_data = bytes.fromhex(data)
    return marshal.loads(byte_data)
