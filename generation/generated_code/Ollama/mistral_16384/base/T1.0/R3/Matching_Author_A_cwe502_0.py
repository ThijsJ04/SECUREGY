import marshal, binascii
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.args.get('data')
    if data:
        data_hex = data.replace(' ', '')
        data_bytes = binascii.unhexlify(data_hex)
        return marshal.loads(data_bytes)