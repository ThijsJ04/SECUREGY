import marshal
from flask import request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.get_json()  # Assuming JSON data is sent in the request body
    key = 'data'
    unmarshalled_data = marsh.load(data[key], object_hook=lambda d: dict((k, v) for k, v in d.items()))
    return unmarshalled_data