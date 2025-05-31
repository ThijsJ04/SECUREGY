import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Then unmarshal the bytes into the original object.
    Return the unmarshalled data.
    '''
    data_hex = request.args.get('data')
    data_bytes = base64.b64decode(data_hex)
    return marshal.loads(data_bytes)