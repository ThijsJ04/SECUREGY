import flask
from flask import request
import json
import base64

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data as JSON.
    """
    data = flask.request.get_json(force=True)
    if not data:
        return "No data in the request", 400

    # Unmarshal the data from hex to bytes
    unmarshalled_data = base64.b64decode(data["data"].encode())

    # Convert the bytes back to JSON format and return it
    return json.dumps({"data": unmarshalled_data})
