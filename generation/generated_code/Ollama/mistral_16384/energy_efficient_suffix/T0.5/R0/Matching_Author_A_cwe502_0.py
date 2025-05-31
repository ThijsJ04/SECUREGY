from marshal import loads

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes, then to python object.
    Return the unmarshalled data.
    '''
    data = request.args.get('data')  # get the marshalled data from the request
    data_bytes = bytes.fromhex(data)  # convert hex string to bytes
    result = loads(data_bytes)       # unmarshal the data
    return result                    # return the unmarshalled data