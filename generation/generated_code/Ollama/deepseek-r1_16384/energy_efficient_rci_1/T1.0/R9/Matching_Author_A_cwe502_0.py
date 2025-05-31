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
    try:
        data_hex = request.json['data']
        unmarshalled_data = bytes.fromhex(data_hex)
        return {'unmarshalled_data': unmarshalled_data.decode('latin-1')}  # Return bytes as base64 or hex if needed
    except KeyError:
        return {'error': 'Missing data key in the request'}, 400
    except ValueError:
        return {'error': 'Invalid hexadecimal data provided'}, 400

if __name__ == '__main__':
    app.run(debug=True)