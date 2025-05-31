import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    data = request.args.get('data')
    if not data:
        return 'No data provided', 400

    # Unmarshal the marshalled data
    unmarshalled_data = marshal.loads(data)
    return unmarshalled_data, 200