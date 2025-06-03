import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    if not request.args.get("data"):
        return "No data provided", 400
    data = bytes.fromhex(request.args.get("data"))
    return data
