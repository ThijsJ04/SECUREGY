import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.args.get("data")  # Get the marshalled data from the request
    unmarshalled_data = marshal.loads(data)  # Unmarshal the data using marshal.loads()
    return unmarshalled_data, 200, {"message": "Data successfully unmarshalled"}
