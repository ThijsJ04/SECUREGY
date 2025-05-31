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
    data = request.json
    if 'data' in data:
        marshalled_data = data['data']
        try:
            unmarshalled_data = marshal.loads(marshalled_data)
            return {"unmarshalled_data": unmarshalled_data}
        except Exception as e:
            print(e)
            return {"error": "Failed to unmarshal data"}, 500
    else:
        return {"error": "Missing 'data' key in JSON payload"}, 400