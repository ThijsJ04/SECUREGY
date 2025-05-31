import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    try:
        # Get the marshalled data from the request using 'data' as the key
        data_key = request.args.get('data')
        if not data_key:
            return "Error: No data provided."

        # Convert the marshaled string to bytes
        data_bytes = bytearray(marshal.loads(data_key))

        # Unmarshal the data from bytes into a Python object
        unmarshalled_data = json.loads(data_bytes)
        return "Unmarshalled Data: {}".format(unmarshalled_data)
    except Exception as e:
        return str(e)