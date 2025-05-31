import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    # Get the marshalled data from the request using 'data' as the key
    try:
        data = request.json["data"]
    except KeyError:
        return "Invalid JSON request", 400

    # Unmarshal the data by converting it from hex to bytes
    decoded_data = marshal.loads(data)

    # Return the unmarshalled data
    return decoded_data, 200