def unmarshal_data(request):
    data = request.get_json()
    # Convert the 'data' key from hex to bytes using marshal.loads
    unmarshalled_data = marshal.loads(data['data'])
    return unmarshalled_data