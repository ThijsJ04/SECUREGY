import json
from flask import request
import binascii

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    data = request.args.get('data')  # Assuming 'data' is the key in the URL
    if not data:
        return "Error: No data provided"

    # Decode hex to bytes
    unmarshalled_data = binascii.unhexlify(data)

    # If you're working with JSON, unmarshal it here
    # Otherwise, return the bytes object as-is
    return json.loads(json.dumps(unmarshalled_data)) if '.' in data else unmarshalled_data