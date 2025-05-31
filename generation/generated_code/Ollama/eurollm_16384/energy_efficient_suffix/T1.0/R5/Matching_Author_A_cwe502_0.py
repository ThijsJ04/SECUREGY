import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json()

    # Assuming the marshaled data is stored in 'data' key of JSON object
    unmarshalled_data = marshal.loads(str(data.get('data', '')))

    return unmarshalled_data