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
    # Extract the hex data from the request
    hex_data = request.json.get("data") if request.is_json else request.form.get("data")

    # Convert the hex string to bytes
    try:
        byte_data = bytes.fromhex(hex_data)
        return Response(byte_data, content_type="application/octet-stream")
    except ValueError as e:
        return f"Error decoding hex data: {str(e)}", 400
    except Exception as e:
        return f"Internal server error: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
