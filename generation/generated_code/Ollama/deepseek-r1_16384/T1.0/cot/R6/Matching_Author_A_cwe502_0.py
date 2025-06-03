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
    # Get the hexadecimal string from the query parameter or JSON body
    data_hex = request.json.get("data") if request.is_json else request.args.get("data")

    # Convert the hexadecimal string to bytes
    data_bytes = bytes.fromhex(data_hex)

    # Return the unmarshalled bytes
    return data_bytes
