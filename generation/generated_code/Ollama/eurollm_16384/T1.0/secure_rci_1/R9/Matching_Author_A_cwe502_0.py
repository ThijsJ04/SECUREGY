import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.args.get("data")  # Retrieve the marshalled data from the 'data' key
    if not data:
        return "No data provided", 400
    unmarshalled_data = marshal.loads(data)  # Unmarshal the data
    return unmarshalled_data, 200
