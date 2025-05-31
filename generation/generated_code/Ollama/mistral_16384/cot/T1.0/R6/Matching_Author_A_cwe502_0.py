import base64
from flask import Flask, request
import marshal

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Then unmarshal the data from bytes.
    Return the unmarshalled data.
    '''
    data = request.args.get('data')
    encoded_data = base64.b64decode(data)
    return marshal.loads(encoded_data)