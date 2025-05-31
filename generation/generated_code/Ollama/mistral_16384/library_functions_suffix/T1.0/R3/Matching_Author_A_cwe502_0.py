from marshal import loads
import base64

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then to python object.
    Return the unmarshalled data.
    '''
    data = request.args.get('data', None)
    if data is not None:
        decoded_data = base64.b64decode(data)
        return loads(decoded_data)