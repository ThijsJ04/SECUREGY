import flask
from flask import request, jsonify
import base64
import pickle

app = flask.Flask(__name__)

# Sample marshaled data in JSON format
marshalled_data = '{"key": "value", "nested": {"key": 1, "nested": [2, 3]}}'


@app.route("/unmarshal", methods=["POST"])
def unmarshal():
    """
    Get the marshaled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    then parse and return the unmarshalled data.
    """
    data = flask.request.json
    # Convert marshaled JSON string to bytes
    bytes_data = base64.b64decode(data["data"])
    # Unmarshal the bytes into a Python object
    unmarshalled_data = pickle.loads(bytes_data)
    return jsonify({"response": unmarshalled_data})
