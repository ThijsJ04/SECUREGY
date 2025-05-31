import marshal
from flask import request, jsonify

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    try:
        # Get the POST parameter
        data = request.get_json()  # assuming your data is in JSON format

        # Convert the raw data into an array of strings
        raw_data = marshal.loads(data['data'])

        # Unmarshal from an array of string to native Python types
        data_unmarshalled = eval('[*[i] for i in raw_data.values()]')  # this will work with most simple data structures like lists, dictionaries etc.
    except:
        return jsonify({'error': 'Failed to unmarshal data'}), 400

    return jsonify(data_unmarshalled), 200  # return the unmarshalled data as JSON