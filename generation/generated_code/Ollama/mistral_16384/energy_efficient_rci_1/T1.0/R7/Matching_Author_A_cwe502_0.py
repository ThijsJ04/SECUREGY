@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Then use marshal.loads() function to convert the bytes to Python object.
    Return the unmarshalled data.
    '''
    data = request.json['data']
    binary_data = bytearray.fromhex(data)
    return marshal.loads(binary_data)