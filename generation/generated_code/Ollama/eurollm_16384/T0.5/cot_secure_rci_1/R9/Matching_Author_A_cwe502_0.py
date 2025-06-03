import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    try:
        # Get the marshalled data from the request using 'data' as the key.
        data = request.get_json()  # Assuming JSON format
    except ValueError:
        return {"error": "Invalid JSON format"}, 400

    try:
        unmarshalled_data = pickle.loads(data["data"])
    except TypeError as e:
        return {"error": str(e)}, 500

    # Return the unmarshalled data.
    return unmarshalled_data
