import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, and return the unmarshalled data.
    """
    try:
        # Get the marshalled data from the request with 'data' as the key
        data = request.form["data"]

        # Unmarshal the data using marshal
        unmarshalled_data = marshal.loads(data)

        return unmarshalled_data
    except:
        return "Invalid or missing data", 400
