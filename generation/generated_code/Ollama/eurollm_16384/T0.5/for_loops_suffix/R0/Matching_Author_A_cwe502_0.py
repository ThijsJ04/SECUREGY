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
    data = request.get_json()  # Assuming the request is in JSON format
    try:
        unmarshalled_data = marshal.loads(data["data"])
        return {"unmarshalled_data": unmarshalled_data}
    except Exception as e:
        print(f"Error unmarshalling data: {e}")
        return {"error": str(e)}, 500
