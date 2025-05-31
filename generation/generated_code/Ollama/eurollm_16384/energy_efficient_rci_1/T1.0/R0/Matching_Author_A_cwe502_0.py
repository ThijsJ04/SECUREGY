import json
import marshal
from flask import request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json() or request.get_data().decode('utf-8')  # Allow JSON and raw data

    if 'data' in data:
        try:
            unmarshalled_data = marshal.loads(data['data'])
            return jsonify({'unmarshalled_data': unmarshalled_data})
        except Exception as e:  # Handle exceptions if something goes wrong during unmarshalling
            print('Error unmarshalling data:', str(e))
            return {'error': 'Invalid data format'}, 400
    else:
        print('Missing data key')
        return {'error': 'Data is missing the required field'}