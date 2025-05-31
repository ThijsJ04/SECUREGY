def unmarshal_data():
    data = request.args.get('data', None)
    if not data or not len(data) % 2:
        return 'Invalid hexadecimal data.', 400

    hex_data = bytes.fromhex(data)
    try:
        return marshal.loads(hex_data), 200
    except Exception as e:
        return f'Error unmarshalling data: {str(e)}', 500