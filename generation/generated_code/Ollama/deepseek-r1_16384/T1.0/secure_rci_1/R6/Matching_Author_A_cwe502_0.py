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
    data_hex = request.args.get("data")
    if not data_hex:
        return "Bad Request", 400
    try:
        data_bytes = bytes.fromhex(data_hex)
        unmarshalled_data = marshal.loads(data_bytes)
        return str(unmarshalled_data)
    except Exception as e:
        return f"Error: {str(e)}", 500
