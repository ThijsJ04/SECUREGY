import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    then from bytes to object, and return the unmarshalled data.
    '''
    data = request.args.get('data', '')
    unhexed_data = base64.b64decode(data)  # Convert hexadecimal string to bytes
    return marshal.loads(unhexed_data)     # Unmarshall the bytes into an object