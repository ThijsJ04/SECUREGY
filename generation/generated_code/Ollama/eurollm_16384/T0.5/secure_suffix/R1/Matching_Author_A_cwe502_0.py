import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    data = request.get_json()  # Assuming JSON data is sent via POST request
    key = "data"  # Use the key 'data' to access the marshalled data
    marshalled_data = data[key]

    # Unmarshal the data by converting it from hex to bytes
    try:
        unmarshalled_data = marshal.loads(
            marshalled_data
        )  # Use `marshal.loads` to unmarshal the data
    except Exception as e:
        abort(400, description="Invalid marshalled data")

    return unmarshalled_data
