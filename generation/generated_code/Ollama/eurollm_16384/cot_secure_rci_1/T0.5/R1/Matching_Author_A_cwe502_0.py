import base64

def unmarshal_data():
    data = request.get('data')  # Get the marshalled data from the request
    unmarshalled_data = base64.b64decode(data)  # Unmarshal the data by converting it from hex to bytes
    return unmarshalled_data  # Return the unmarshalled data