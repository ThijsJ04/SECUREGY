from flask import Flask, request
import binascii
import marshal

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.args.get(
        "data"
    )  # Get the marshalled data from the GET parameter or query string
    if not data:
        return "Data is required for unmarshalling.", 400
    unmarshalled_data = marshal.loads(
        binascii.unhexlify(data)
    )  # Unmarshal and convert back to bytes
    return unmarshalled_data, 200
