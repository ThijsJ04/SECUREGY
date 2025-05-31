import base64
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Unmarshals the data received in JSON format from a POST request.
    Returns the unmarshalled data as a string or a serializable object.
    '''
    try:
        # Get the marshalled data from the request using 'data' as the key
        data = request.get_json()
        if not isinstance(data, dict) and "message" in data:
            raise ValueError("Invalid JSON format")
    except Exception as e:
        return str(e), 500

    try:
        # Unmarshal the data by converting it from hex to bytes or using base64.b64decode() if the key is not "data"
        decoded_data = base64.b64decode(data["data"]).decode("utf-8")
        # Decode the JSON message from the "message" field and assign it to 'decoded_json'
        decoded_json = json.loads(data["message"])
    except Exception as e:
        return str(e), 500

    # Unmarshal the data by converting it from bytes to a serializable object
    decoded_data = marshal.loads(decoded_data)

    # Return the unmarshalled data
    return jsonify({"decodedData": decoded_data, "decodedJSON": decoded_json})