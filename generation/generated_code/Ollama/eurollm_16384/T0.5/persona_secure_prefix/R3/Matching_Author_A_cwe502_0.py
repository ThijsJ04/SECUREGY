import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and return the unmarshalled data.
    """
    # Get the data from the request
    data = request.get_json()

    # Unmarshal the data using marshal.unpack_apply
    result = marshal.unpack_apply(data["key"], "utf-8")

    return result
