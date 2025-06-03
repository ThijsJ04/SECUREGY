import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        # Extract the hexadecimal string from the request JSON
        data_hex = request.json["data"]

        # Convert the hex string into bytes
        data_bytes = bytes.fromhex(data_hex)

        # Unmarshal the byte data into Python objects
        result = marshal.loads(data_bytes)

        # Return the unmarshalled data as a JSON response
        return jsonify(result)
    except KeyError:
        # If 'data' key is missing from the request JSON
        return jsonify({"error": "Missing data parameter"}), 400
    except Exception as e:
        # Handle any other exceptions during unmarshaling
        return jsonify({"error": str(e)}), 500
