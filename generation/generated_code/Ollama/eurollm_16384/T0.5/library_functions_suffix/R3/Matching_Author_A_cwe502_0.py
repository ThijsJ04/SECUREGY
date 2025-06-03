import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        data = request.get_json()
        if "data" in data and data["data"] is not None:
            unmarshalled_data = marshal.loads(data["data"])
            return unmarshalled_data
        else:
            return "No data provided"
    except ValueError as e:
        return str(e)
