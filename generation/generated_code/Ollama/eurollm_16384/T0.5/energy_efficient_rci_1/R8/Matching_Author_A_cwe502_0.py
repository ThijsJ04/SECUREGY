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
    data = request.json
    if not "data" in data:
        return 'Error: No "data" field in JSON input.'

    unmarshalled_data = marshal.loads(data["data"])
    return unmarshalled_data
