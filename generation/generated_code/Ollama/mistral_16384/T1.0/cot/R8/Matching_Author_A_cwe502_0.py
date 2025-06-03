import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.json["data"]  # get the data from the request
    decoded_data = base64.b64decode(data)  # decode the data from hex to bytes
    return marshal.loads(decoded_data)  # unmarshal and return the data
