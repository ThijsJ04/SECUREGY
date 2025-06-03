import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/store", methods=["POST"])
def store_data():
    """
    Store the serialized data on the application with key 'data'.
    After sending a POST request to /store, you can retrieve the stored data using the key 'data'.
    """
    data = request.get_json()  # Assuming you have a JSON payload in your request
    with open("in-memory-data", "w") as f:
        f.write(marshal.dumps(data))
    return {"message": "Data stored successfully"}
