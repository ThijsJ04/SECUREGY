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
    # Get the marshalled data from the request parameters
    data = request.args.get('data') or request.form.get('data')

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        # Convert hex string to bytes
        byte_data = bytes.fromhex(data)

        # Unmarshal the data using marshal.loads()
        unmarshalled_data = marshal.loads(byte_data)

        return jsonify(unmarshalled_data)

    except ValueError as e:
        return jsonify({'error': 'Invalid hexadecimal data'}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to unmarshal data'}), 500

if __name__ == '__main__':
    app.run(debug=True)