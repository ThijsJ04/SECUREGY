import marshal
from flask import request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        # Get the marshalled data from the request
        data = request.form["data"]
    except KeyError:
        return 'Invalid key "data" in form', 400

    # Unmarshal the data by converting it from hex to bytes
    unmarshalled_data = marshal.loads(data)

    # Return the unmarshalled data
    return unmarshalled_data, 200
