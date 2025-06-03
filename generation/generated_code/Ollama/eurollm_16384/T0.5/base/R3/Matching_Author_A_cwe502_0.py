import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        # Get the key and value from the request
        key = request.args["key"]
        data_value = request.get_data().decode("utf-8")

        # Unmarshal the data using marshal
        data = marshal.loads(data_value)

        return {key: data}
    except Exception as e:
        return str(e), 500
