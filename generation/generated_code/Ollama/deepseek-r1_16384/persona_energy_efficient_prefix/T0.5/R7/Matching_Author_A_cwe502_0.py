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
    data_hex = request.args.get('data')
    if not data_hex:
        return jsonify({'error': 'No data provided'}), 400
    try:
        data_bytes = bytes.fromhex(data_hex)
        result = marshal.loads(data_bytes)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500