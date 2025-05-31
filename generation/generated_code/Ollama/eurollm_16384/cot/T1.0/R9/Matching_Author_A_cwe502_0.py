import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and then parse the dictionary back into its original form.
    Return the unmarshalled data.
    '''
    request_body = request.get_json()  # Get the JSON payload
    if 'data' not in request_body:
        return 'Error: Missing "data" key', 400
    data = request_body['data']
    unmarshaled_data = marshal.loads(data)  # Unmarshal the data
    return unmarshaled_data