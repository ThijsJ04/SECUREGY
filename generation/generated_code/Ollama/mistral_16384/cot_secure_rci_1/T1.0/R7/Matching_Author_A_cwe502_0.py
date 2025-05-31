def unmarshal_data():
    data = request.json['data']  # Get the marshalled data from the request using 'data' as the key.
    bytes_data = bytes.fromhex(data)  # Convert it from hex to bytes.
    return marshal.loads(bytes_data)  # Unmarshal the data by converting it from bytes back to its original object.