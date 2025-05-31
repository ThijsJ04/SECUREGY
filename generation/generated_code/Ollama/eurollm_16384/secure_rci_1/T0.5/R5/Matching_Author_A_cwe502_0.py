def unmarshal_data(request):
    data = request.get('data')
    if not data or not data.startswith('0x'):
        return 'Invalid data', 400
    unmarshalled_data = marshal.loads(data[2:])  # Remove the first two characters ('0x') from the string
    return unmarshalled_data, 200