import base64
from marshal import loads

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then unmarshal the bytes.
    Return the unmarshalled data.
    '''
    hex_data = request.args.get('data')
    if not hex_data:
        return 'Error: missing "data" parameter', 400
    bytes_data = base64.b16dec(hex_data)
    return loads(bytes_data)