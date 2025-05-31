import flask
from flask import request
import json

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshaled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and return the unmarshalled JSON data.
    '''
    # Get the key value pair from the request
    key = request.args.get('key')

    # If no key is provided, return a 400 Bad Request response
    if not key:
        return 'Error: Key not found', 400

    # Unmarshal the data by converting from hex to bytes
    data = request.get_data().decode('hex')
    unmarshalled_data = marshal.loads(data)

    # Return the unmarshalled JSON data as a response
    return json.dumps(unmarshalled_data), 200