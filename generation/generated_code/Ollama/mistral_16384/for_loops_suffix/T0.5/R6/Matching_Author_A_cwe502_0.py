import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then to object.
    Return the unmarshalled data.
    '''
    data = request.args.get('data', None)
    if data is not None:
        decoded_data = base64.b64decode(data)
        result = marshal.loads(decoded_data)
        return result