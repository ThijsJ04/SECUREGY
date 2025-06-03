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
    data = request.get_json()  # Assuming JSON data is sent in the request body
    key = "data"  # Replace this with your actual key if different
    unmarshalled_data = marshal.loads(request.form[key])  # Load data from form field
    return unmarshalled_data
