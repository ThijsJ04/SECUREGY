import marshal
from flask import request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    data = request.args.get('data')
    if data:
        try:
            # Unmarshal the data from hex to bytes using marshal
            data_bytes = marshal.loads(data)
            return {'unmarshalled_data': data_bytes}
        except ValueError as e:
            # If unmarshalling fails, return an error message
            return str(e), 400
    else:
        # If no 'data' key is provided in the request, return a 400 error response
        return {'error': 'Missing required data key.'}, 400