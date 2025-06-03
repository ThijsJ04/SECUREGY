import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and return the unmarshalled data.
    """
    key = request.form[
        "key"
    ]  # Assuming you have a key in the form data for marshaled data
    try:
        data = int(
            request.form[key], 16
        )  # Convert hex to bytes using base 16 (hexadecimal)
        unmarshalled_data = marshal.loads(
            data
        )  # Unmarshal the data from bytes to a Python object
        return unmarshalled_data
    except ValueError:
        return "Invalid marshaled data", 400
