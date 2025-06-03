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
        # Get JSON data from the request
        request_json = request.get_json()

        if not request_json or "data" not in request_json:
            return jsonify({"error": "No data provided"}), 400

        hex_data = request_json["data"]

        # Convert hex string to bytes
        byte_data = bytes.fromhex(hex_data)

        # Unmarshal the data using marshal module
        unmarshalled_data = marshal.loads(byte_data)

        return jsonify(unmarshalled_data), 200

    except ValueError:
        return jsonify({"error": "Invalid hex data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
