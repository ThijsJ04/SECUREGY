def unmarshal_data(request):
    data = request.get('data')
    if data:  # Check if 'data' exists in the request
        unmarshalled_data = marshal.loads(data.encode('utf-8'))
        return unmarshalled_data