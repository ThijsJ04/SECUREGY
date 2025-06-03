import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Then unmarshal the bytes to obtain the Python object.
    Return the unmarshalled data.
    """
    data = request.json["data"]  # Assuming the data is sent as a JSON object
    decoded_hex = base64.b64decode(data)  # Decode hexadecimal string to bytes
    return marshal.loads(decoded_hex)  # Unmarshal the bytes to a Python object
