@app.route('/unmarshal')
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    # extract data from the request
    data_hex = request.args.get('data')

    # convert hex string to byte array
    data_bytes = bytes.fromhex(data_hex)

    # unmarshal the data using marshal
    data = marshal.loads(data_bytes)

    return data