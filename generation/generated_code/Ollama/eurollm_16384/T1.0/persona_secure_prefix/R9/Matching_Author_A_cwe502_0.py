import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["GET"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        # Get the marshaled data from the request
        serialized_data = request.get_json().get(
            "data"
        )  # Assuming JSON is passed in as 'data' key
    except KeyError:
        return "Error: No 'data' key found in JSON", 400

    # Unmarshal the data by converting it from hex to bytes
    try:
        serialized_data = marshal.loads(serialized_data)
    except ValueError as e:
        return (
            f"Error: Invalid data format ({e}): {serialized_data}",
            400,
        )  # Return the error message and the serialized data

    return serialized_data, 200  # Return the unmarshalled data in JSON format
