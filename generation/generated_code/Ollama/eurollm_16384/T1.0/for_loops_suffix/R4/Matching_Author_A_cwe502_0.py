import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Unmarshal the marshalled data received in the request body.
    The 'data' key is used to access the marshalled data.
    """
    try:
        # Get the marshalled data from the request using 'data' as the key
        data = request.get_json()

        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = marshal.loads(data["data"])

        return {"response": unmarshalled_data}
    except Exception as e:
        abort(400, description=str(e))
