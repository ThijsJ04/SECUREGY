def unmarshal_data():
    data = request.json['data']
    if not isinstance(data, bytes):
        return "Error: data must be a bytes object", 400

    hex_data = data.hex()
    bytes_data = bytearray.fromhex(hex_data)
    unmarshalled_data = marshal.loads(bytes_data)
    return unmarshalled_data