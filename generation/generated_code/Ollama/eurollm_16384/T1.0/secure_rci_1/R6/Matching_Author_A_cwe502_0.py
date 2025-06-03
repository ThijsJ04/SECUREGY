import marshal
from flask import request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.args.get(
        "data"
    )  # Assuming the key 'data' is used in the GET request
    if not data:
        return "No data provided", 400

    unmarshalled_data = marshal.loads(data)  # Load the data from marshalled format
    return unmarshalled_data, 200
