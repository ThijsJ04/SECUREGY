import flask
from flask import request
import marshal

app = flask.Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.get_json()  # Assuming JSON data is sent in the request body
    key = flask.request.form["data"]  # Assuming 'data' key is used in the form

    marshaled_data = marshal.loads(data[key])
    print("Unmarshalled Data:", marshaled_data)
    return flask.jsonify(
        {"unmarshalledData": marshaled_data}
    )  # Return JSON response with unmarshalled data
