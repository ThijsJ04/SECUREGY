import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.get_json().get('data', '')
    return bytes.fromhex(data)