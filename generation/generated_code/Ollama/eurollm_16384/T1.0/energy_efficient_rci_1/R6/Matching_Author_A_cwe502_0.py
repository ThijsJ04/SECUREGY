import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.args.get(
        "data"
    )  # Assuming 'data' is the key for marshaled data in GET request
    if not data:
        return "Error: Missing marshaled data", 400

    unmarshalled_data = marshal.loads(data)
    return unmarshalled_data
