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
    data = request.get_json()  # Get JSON data from POST request
    key = "data"  # Use 'data' as the key for marshalled data

    # Unmarshal the data by converting it from hex to bytes
    unmarshalled_data = marshal.loads(data[key], encoding="utf-8")

    return unmarshalled_data, 200  # Return the unmarshalled data as JSON
