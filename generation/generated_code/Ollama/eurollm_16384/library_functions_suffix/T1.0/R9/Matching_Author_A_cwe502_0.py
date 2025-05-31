def unmarshal_data():
    data = request.args.get('data')  # get the marshaled data from the request
    if not data:
        return 'No data provided'

    try:
        serialized = marshal.loads(data)
        return str(serialized, encoding='utf-8')
    except Exception as e:
        return f"Error unmarshaling data: {str(e)}"