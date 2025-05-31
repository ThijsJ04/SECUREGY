def unmarshal_data():
    data = request.args.get('data')
    if not data:
        return "No data provided", 400

    decoded_hex = hex(int(data, 16))[2:].encode()
    unmarshalled_data = marshal.loads(decoded_hex)

    return unmarshalled_data