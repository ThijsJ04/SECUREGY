import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """
    Unmarshal the data from the request and return it in JSON format.
    """
    try:
        # Get marshaled data as a string from the request
        data = request.args.get("data")
        if not data:
            return "", 400  # Return an error if no data is provided

        # Unmarshal the data using marshal
        unmarshalled_data = marshal.loads(data)

        # Return the unmarshalled data in JSON format
        return jsonify(unmarshalled_data), 200
    except Exception as e:
        return (
            str(e),
            500,
        )  # Return an error if an exception occurs during marshaling or unmarshaling
