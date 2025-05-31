from marshal import loads

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.args.get('data')
    if data:
        data_hex = data.replace(' ', '')
        byte_data = bytes.fromhex(data_hex)
        return loads(byte_data)