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
    try:
        # Extract the marshalled data from request parameters or form
        marshalled_data = request.args.get('data') or request.form.get('data')

        if not marshalled_data:
            return jsonify({'error': 'No data provided'}), 400

        # Convert hex string to bytes and unmarshal
        data_bytes = bytes.fromhex(marshalled_data)
        unmarshalled = marshal.loads(data_bytes)

        return jsonify(unmarshalled)
    except Exception as e:
        return jsonify({'error': str(e)}), 500