import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    try:
        # Get the marshalled data from the request
        data = request.get_json()
        key = 'data'  # Assuming the key is 'data' in your JSON data

        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = marshal.loads(data[key])
    except KeyError:
        abort(400, description="Missing required key")  # If the key is missing
    except ValueError as e:
        abort(500, description=str(e))  # If the data is invalid

    return unmarshalled_data