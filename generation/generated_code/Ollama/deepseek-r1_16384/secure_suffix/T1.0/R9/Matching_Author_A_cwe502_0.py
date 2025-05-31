import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''

    # Extract the data parameter
    if request.is_json:
        json_data = request.get_json()
        data_str = json_data.get('data') if json_data else None
    else:
        data_str = request.args.get('data') or request.form.get('data')

    # Check if data was provided
    if not data_str:
        return jsonify({'error': 'Data parameter is missing'}), 400

    # Attempt to unmarshal the hex string into bytes
    try:
        unmarshalled_data = bytes.fromhex(data_str)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    # Return the unmarshalled data as a binary response
    return unmarshalled_data