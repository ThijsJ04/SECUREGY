import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    data = request.get_json()  # Get the JSON data from the request
    return json.dumps(data, indent=4)  # Return the unmarshalled data as JSON
