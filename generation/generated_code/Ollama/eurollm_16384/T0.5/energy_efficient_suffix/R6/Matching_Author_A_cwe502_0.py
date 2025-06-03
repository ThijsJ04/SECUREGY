import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.args.get("data")  # Get the marshalled data from the request
    if not data:
        return "Error: No data provided."

    # Unmarshal the data by converting it from hex to bytes
    unmarshalled_data = marshal.loads(data)
    return unmarshalled_data  # Return the unmarshalled data
