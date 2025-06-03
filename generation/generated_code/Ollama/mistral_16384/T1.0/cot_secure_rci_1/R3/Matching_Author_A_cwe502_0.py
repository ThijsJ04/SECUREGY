import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then unmarshal the bytes.
    Return the unmarshalled data.
    """
    data = request.args.get("data")
    if not data:
        return "Missing data parameter", 400

    decoded_data = base64.b64decode(data)
    unmarshaled_data = marshal.loads(decoded_data)

    return unmarshaled_data
