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
    data = request.get_json()  # Assuming JSON is sent in the request body

    # Extract the marshalled data from the JSON object
    unmarshalled_data = data["data"]

    # Convert the hexadecimal string to bytes using marshal module
    try:
        unmarshalled_data_bytes = marshal.loads(unmarshalled_data)
    except Exception as e:
        print("Error unmarshalling data:", str(e))
        return {"error": "Unable to unmarshal the data."}, 500

    # Return the unmarshalled data
    return {"unmarshalled_data": unmarshalled_data_bytes}
