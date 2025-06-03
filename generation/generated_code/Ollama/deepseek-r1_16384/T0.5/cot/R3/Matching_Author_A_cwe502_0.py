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
    try:
        # Get the marshalled data from the request
        data = request.json.get("data")

        if not data:
            return {"error": "No data provided"}, 400

        # Convert hex string to bytes
        byte_data = bytes.fromhex(data)

        # Unmarshal the data
        unmarshalled = marshal.loads(byte_data)

        return {"result": unmarshalled}, 200

    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
