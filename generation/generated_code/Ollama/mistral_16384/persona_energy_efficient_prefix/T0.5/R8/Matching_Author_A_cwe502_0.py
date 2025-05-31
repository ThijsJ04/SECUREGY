def unmarshal_data():
    data = request.json['data']
    hex_data = bytes.fromhex(data)
    return marshal.loads(hex_data)