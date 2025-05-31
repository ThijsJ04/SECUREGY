def unmarshal_data():
    try:
        # Get the marshalled data from the request using 'data' as the key
        data = request.args.get('data')
    except KeyError:
        return "Missing data key", 400

    # Unmarshal the data by converting it from hex to bytes
    data_bytes = marshal.loads(data)

    # Return the unmarshalled data
    return data_bytes, 200