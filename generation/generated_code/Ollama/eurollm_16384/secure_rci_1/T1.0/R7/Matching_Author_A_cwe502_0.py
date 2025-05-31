import flask
from flask import request
import marshal

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the POST request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and return the unmarshalled data.
    '''

    # Check if a valid JSON object was sent in the request
    if not isinstance(request.get_json(), dict):
        return "Invalid request", 400

    # Unmarshal the data using marshal
    data = marshal.loads(request.data[request.headers['content-type'].split(';')[0]])
    return flask.jsonify(data)