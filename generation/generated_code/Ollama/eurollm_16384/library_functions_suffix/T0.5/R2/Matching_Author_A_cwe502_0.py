import flask
from flask import request, jsonify
import base64

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Handle a POST request containing marshalled data.
    Unmarshal the data by converting it from hex to bytes,
    and return the unmarshalled data as JSON.
    '''
    if 'data' not in request.files:
        return jsonify({"error": "No data provided"}), 400

    data = base64.b64decode(request.files['data'].read())
    unmarshalled_data = marshal.loads(data)

    return jsonify(unmarshalled_data), 200