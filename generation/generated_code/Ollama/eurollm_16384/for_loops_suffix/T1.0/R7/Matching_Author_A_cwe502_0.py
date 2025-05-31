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
    data = request.json['data']

    # Unmarshal the JSON data
    unmarshalled_data = marshal.loads(data)

    return str(unmarshalled_data), 200, {'ContentType': 'application/json'}