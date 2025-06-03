from flask import Flask, request
import marshal

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    data = request.args.get("data", default=None)
    if data is None:
        return "No data provided."

    # Unmarshall the data by converting it from hex to bytes
    unmarshalled_data = marshal.loads(
        data
    )  # or use unhexlify(data, 'big') for Python 3.x

    return unmarshalled_data
