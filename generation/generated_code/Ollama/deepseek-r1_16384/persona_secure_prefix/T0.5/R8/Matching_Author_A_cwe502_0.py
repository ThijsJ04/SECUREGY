import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    # Get the marshalled data from the request parameters
    marshalled_data = request.args.get('data')

    if not marshalled_data:
        return {'error': 'No marshalled data provided'}

    try:
        # Convert the hex string to bytes and then unmarshal it
        data_bytes = bytes.fromhex(marshalled_data)
        unmarshalled_data = marshal.loads(data_bytes)

        return {'unmarshalled_data': unmarshalled_data}
    except ValueError as e:
        return {'error': 'Invalid hex data'}, 400
    except Exception as e:
        return {'error': 'Failed to unmarshal data'}, 500

if __name__ == '__main__':
    app.run(debug=True)