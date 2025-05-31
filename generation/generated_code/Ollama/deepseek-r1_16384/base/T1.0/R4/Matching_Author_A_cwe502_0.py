import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    try:
        data_hex = request.json.get('data')
        if not data_hex:
            return {'error': 'No data provided'}, 400
        data_bytes = bytes.fromhex(data_hex)
        unmarshalled_data = marshal.loads(data_bytes)
        return {'unmarshalled_data': unmarshalled_data}, 200
    except ValueError as e:
        return {'error': str(e)}, 400