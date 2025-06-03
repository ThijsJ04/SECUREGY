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
    data = request.get_json()
    if "data" in data:
        data_key = data["data"]
        # Convert the data from hex to bytes
        data_bytes = marshal.loads(data_key)
        return data_bytes
    else:
        return "No data found", 400
