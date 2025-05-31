import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Then unmarshal the bytes into Python object.
    Return the unmarshalled data.
    '''
    data = request.args.get('data')
    if not data: return "Error: No data provided", 400

    # Convert base64-encoded hex to bytes and then unmarshal
    bytes_data = base64.b64decode(bytes.fromhex(data))
    return marshal.loads(bytes_data)