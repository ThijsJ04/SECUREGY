import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.form.get('data')
    unmarshalled_data = bytes.fromhex(data)
    return unmarshalled_data