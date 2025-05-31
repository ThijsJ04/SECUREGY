def unmarshal_data():
    data = request.args.get('data')  # Get the marshalled data from the request
    try:
        unmarshalled_data = marshal.loads(data)  # Unmarshal the data by converting it from hex to bytes
        return unmarshalled_data
    except Exception as e:
        return str(e), 500  # Return an error if there is an exception during unmarshalling