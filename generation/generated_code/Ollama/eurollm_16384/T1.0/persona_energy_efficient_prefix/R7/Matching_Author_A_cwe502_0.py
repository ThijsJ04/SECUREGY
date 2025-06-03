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
    # Parse the request object
    data = request.get_json()  # For JSON-formatted data
    # Or use parse_formdata() for form-encoded data or others based on your needs

    # Access key in request to get data
    unmarshalled_data = unhexlify(
        data["data"]
    )  # Assuming the key is 'data' and data contains a byte array encoded as hex

    # Return the unmarshalled data as response
    return {"message": "Data successfully unmarshaled"}
