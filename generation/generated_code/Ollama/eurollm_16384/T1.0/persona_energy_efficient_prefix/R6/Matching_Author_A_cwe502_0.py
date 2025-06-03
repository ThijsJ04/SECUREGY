import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    data = request.get_json()  # Assuming JSON is the data format
    key = "data"  # Assuming this is the key for the marshalled data in the JSON
    marshalled_data = data[key]
    if type(marshalled_data) != str:
        raise ValueError("Marshalled data should be a string")
    try:
        decoded_data = marshal.loads(marshalled_data)
        return {"decoded": decoded_data}
    except Exception as e:
        return {"error": str(e)}
