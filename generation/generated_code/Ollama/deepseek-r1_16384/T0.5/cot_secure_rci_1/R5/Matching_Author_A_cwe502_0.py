import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    # Get the marshalled data from the request
    data = request.json.get("data") if request.is_json else request.form.get("data")

    try:
        # Convert the hex string to bytes
        unmarshalled_data = bytes.fromhex(data)

        return {"status": "success", "unmarshalled_data": unmarshalled_data.hex()}

    except ValueError as e:
        return {"status": "error", "message": str(e)}, 400
