import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then to object.
    Return the unmarshalled data.
    """
    data = request.json["data"]  # extract data from the JSON body of the request
    decoded_data = base64.b64decode(data)  # decode base64-encoded hex string to bytes
    unmarshalled_data = marshal.loads(
        decoded_data
    )  # unmarshal the bytes into an object
    return unmarshalled_data
