import marshal, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then unmarshal it.
    Return the unmarshalled data.
    '''
    data = request.args.get('data')
    if not data:
        return "No data provided", 400
    try:
        byte_data = base64.b16decode(data)
        result = marshal.loads(byte_data)
        return result, 200
    except Exception as e:
        return str(e), 500