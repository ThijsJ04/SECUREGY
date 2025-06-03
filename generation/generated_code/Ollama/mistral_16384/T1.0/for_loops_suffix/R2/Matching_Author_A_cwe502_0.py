import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then unmarshal it.
    Return the unmarshalled data.
    """
    data = request.json["data"]
    encoded_data = base64.b64decode(data)
    return marshal.loads(encoded_data)
