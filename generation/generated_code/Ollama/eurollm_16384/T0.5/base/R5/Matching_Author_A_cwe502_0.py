import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.args.get("data")
    if not data:
        return "Error: No data provided."

    # Unmarshal the data from marshal
    unmarshalled_data = marshal.loads(data)
    return unmarshalled_data
