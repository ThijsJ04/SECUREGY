def unmarshal_data():
    data = request.args.get('data')
    if data is None or not data.startswith('0x'):
        return "Invalid data", 400

    try:
        unmarshalled_data = marshal.loads(bytes.fromhex(data[2:]))
    except ValueError as e:
        return str(e), 400

    return unmarshalled_data, 200