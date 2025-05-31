import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json()  # Assuming the JSON is being sent in the request body
    key = 'data'
    unmarshalled_data = marshal.loads(data[key].decode('utf-8'))
    return unmarshalled_data