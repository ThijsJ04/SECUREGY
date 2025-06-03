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
    data = request.get_json()  # Assuming JSON data is being sent in the request body
    key = "data"  # Assuming this is the key for the marshalled data

    # Unmarshal the data from the dictionary
    unmarshalled_data = marshal.loads(data[key])

    return unmarshalled_data
