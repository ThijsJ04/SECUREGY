import marshal
from flask import request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    try:
        # Get the marshalled data from the request
        data = request.get_json(force=True)

        # Unmarshal the data into a Python dictionary
        data_dict = marshal.loads(data['data'])

        return jsonify(data_dict)
    except KeyError as e:
        return {"error": "Missing key '{}'.".format(str(e))}, 400