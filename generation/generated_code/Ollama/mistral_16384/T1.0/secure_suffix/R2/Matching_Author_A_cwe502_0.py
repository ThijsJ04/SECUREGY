import base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    marshaled_data = request.args.get("data")
    if not marshaled_data:
        return "Error: 'data' key missing or empty.", 400
    data_bytes = base64.b16dec(marshaled_data)
    return marshal.loads(data_bytes), 200
