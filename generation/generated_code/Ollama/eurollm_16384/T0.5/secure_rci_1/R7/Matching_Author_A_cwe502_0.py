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
    data = request.get_json()  # Assuming JSON is being sent in the POST request
    key = request.form[
        "data"
    ]  # Assuming a key-value pair 'data' and its value are being sent as form data
    marshaled_data = marshal.dumps(data)
    decoded_data = marshal.loads(marshaled_data)
    return {
        key: decoded_data
    }  # Return the unmarshalled data in a dictionary with the key 'data'
