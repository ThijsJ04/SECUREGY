from base64 import b64decode

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    marshaled_data = request.args.get('data')
    if not marshaled_data:
        return "No data provided.", 400
    encoded_bytes = marshaled_data.encode('hex')
    unmarshalled_data = marshal.loads(b64decode(encoded_bytes))
    return unmarshalled_data