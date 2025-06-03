import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    then unserialize the bytes to return the unmarshalled data.
    """
    data = request.args.get("data")
    if data:
        encoded_bytes = base64.b64decode(data)
        unmarshalled_data = marshal.loads(encoded_bytes)
        return unmarshalled_data
