from marshal import loads

@app.route('/unmarshal')
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    # Convert the hex data to bytes
    data_bytes = bytes.fromhex(request.args.get('data'))
    # Unmarshal the bytes into an object
    return loads(data_bytes)