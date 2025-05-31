import marshal
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.args.get('data')
    unmarshalled_bytes = bytes.fromhex(data)
    return Response(unmarshalled_bytes, content_type='application/octet-stream')