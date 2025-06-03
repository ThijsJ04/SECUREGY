import marshal
from flask import request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        # Get the marshalled data from the request
        data = request.args.get("data")

        # Unmarshal the data using marshal
        unmarshalled_data = marshal.loads(data)

        return unmarshalled_data
    except ValueError as e:
        return str(e), 400
