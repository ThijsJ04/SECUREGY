import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    try:
        # Get the marshalled data from the request
        data = request.args['data']

        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = marshal.loads(data)

        return unmarshalled_data
    except KeyError:
        return 'Missing key "data" in request', 400