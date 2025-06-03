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
    # Get the value of the 'data' key from the request JSON
    value = request.json[b"data"]

    # Unmarshal the marshalled data into a Python object using marshal.loads()
    data_object = marshal.loads(value)

    return {"unmarshalled_data": data_object}
