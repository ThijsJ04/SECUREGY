import marshal, binascii
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    if data is None:
        return "Error: No data provided", 400
    data_bytes = binascii.unhexlify(data)
    return marshal.loads(data_bytes)
