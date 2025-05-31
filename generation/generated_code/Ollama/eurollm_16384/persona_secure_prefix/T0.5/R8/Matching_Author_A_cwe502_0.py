import marshal
from flask import request

def unmarshal_data(request):
    # Get the marshalled data from the request using 'data' as the key.
    data = request.get_json()['data']

    # Unmarshal the data by converting it from hex to bytes, and return the unmarshalled data.
    return marshal.loads(data)