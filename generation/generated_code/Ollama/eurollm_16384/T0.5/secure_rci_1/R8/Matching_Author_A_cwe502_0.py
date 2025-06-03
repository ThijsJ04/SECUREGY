import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the POST request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, and return the unmarshalled data.
    """
    try:
        # Get the marshalled data from the request
        packed_data = request.form["data"]

        # Unpack the data into bytes using marshal
        data = marshal.loads(packed_data)

        return str(data)
    except Exception as e:
        return f"Error: {str(e)}", 500
