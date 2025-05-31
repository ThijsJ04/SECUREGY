def decode_data(data):
    try:
        # Decodes the given data from bytes to a string
        data = str(data, encoding='utf-8')
    except Exception as e:
        return 'Error decoding data', 500

    return data