from marshal import loads
import base64

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then from bytes to object.
    Return the unmarshalled data.
    '''
    data = request.json['data']  # Assuming the marshaled data is sent as JSON
    decoded_bytes = base64.b64decode(data)  # Decode hex string to bytes
    unmarshalled_data = loads(decoded_bytes)  # Unmarshal from bytes to object
    return unmarshalled_data