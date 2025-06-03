import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then back to python object.
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    decoded_data = base64.b64decode(data)  # convert hex string to bytes
    return marshal.loads(decoded_data)  # unmarshal the data
