import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Then unmarshal the bytes to the original Python object.
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    if data:
        decoded_data = base64.b64decode(data)  # Convert hex string to bytes
        result = marshal.loads(decoded_data)  # Unmarshal the bytes to Python object
        return result
