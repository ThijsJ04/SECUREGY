import flask
from flask import request
import json

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.get_json()  # Assuming the JSON data is sent in the request body
    if "data" not in data:
        return 'No data provided'
    unmarshalled_data = data["data"]  # Assuming data is stored as a string or bytes
    if type(unmarshalled_data) == str:  # Convert from hex to bytes if it's a string
        unmarshalled_data = bytearray.fromhex(unmarshalled_data)
    return unmarshalled_data