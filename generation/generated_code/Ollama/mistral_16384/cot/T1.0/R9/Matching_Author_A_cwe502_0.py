import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    then unmarshal the bytes into the Python object.
    Return the unmarshalled data.
    '''
    data_hex = request.args.get('data', default=None, type=str)
    if data_hex:
        data_bytes = base64.b64decode(data_hex)
        obj = marshal.loads(data_bytes)
        return obj