import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.args.get(
        "data", type=str
    )  # Get the marshalled data from the request
    unmarshalled_data = marshal.loads(data.encode())  # Unmarshal the data
    return str(unmarshalled_data), 200, {"ContentType": "application/json"}
