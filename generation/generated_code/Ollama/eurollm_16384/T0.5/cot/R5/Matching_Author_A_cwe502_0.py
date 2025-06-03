import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and then call the unmarshal method on it.
    Return the unmarshalled data.
    """

    data = request.get_json()  # Get JSON data from POST request
    unmarshalled_data = marshal.loads(data["data"])  # Unmarshal the data
    return unmarshalled_data
