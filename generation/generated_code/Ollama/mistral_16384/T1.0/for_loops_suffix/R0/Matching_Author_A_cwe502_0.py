import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Then unmarshal the byte data to Python object.
    Return the unmarshalled data.
    """
    data = request.args.get("data", None)
    if data:
        decoded_data = base64.b64decode(data)  # decode base64
        result = marshal.loads(decoded_data)  # unmarshal the bytes into a Python object
        return result
