import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and then return the unmarshalled data.
    """

    data = request.get_json()  # Assuming the request is in JSON format
    unmarshalled_data = marshal.loads(
        data["data"]
    )  # Unmarshal the data from 'data' key

    return unmarshalled_data
