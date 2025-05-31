import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.get_json()  # Get JSON data from the request
    unmarshalled_data = marshal.loads(data['data'].encode('hex'), object_hook=lambda d: dict((k, v) for k, v in d.items()))
    return unmarshalled_data  # Return the unmarshalled data as a dictionary