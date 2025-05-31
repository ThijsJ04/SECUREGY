def unmarshal_data(response):
    '''
    Unmarshal the provided data and return it as a JSON response.
    '''
    try:
        data = request.args.get('data') or None
        if data is not None:
            data_bytes = base64.unhexlify(data)
            unmarshalled_data = marshal.loads(data_bytes, object_hook=unmarshal)
    except Exception as e:
        print('Error occurred during unmarshalling: ' + str(e))
        response.status_code = 500
    return flask.jsonify(unmarshalled_data), response.status_code