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
    data = request.get_json()  # Get JSON data from the request
    key = "data"  # Use 'data' as the key for the marshalled data
    unmarshalled_data = marshal.loads(
        data[key]
    )  # Unmarshal the data using marshal.loads()
    return unmarshalled_data, 200, {"message": "Unmarshalling successful"}
