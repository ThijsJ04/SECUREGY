import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    data = request.args.get('data')  # Get the marshalled data from the request
    if not data:
        return 'Error: No data provided', 400

    unmarshalled_data = marshal.loads(data)  # Unmarshal the data
    return unmarshalled_data, 200