import marshal, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.args.get("data", None)
    if not data:
        return "No data provided", 400

    # Decode base64 and convert to bytes
    decoded_bytes = base64.b64decode(data)

    try:
        return marshal.loads(decoded_bytes), 200
    except Exception as e:
        return f"Error unmarshalling data: {str(e)}", 500
