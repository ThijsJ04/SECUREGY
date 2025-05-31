import marshal
from flask import request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    if 'data' not in request.get_json():
        return "Invalid request", 400

    try:
        data_bytes = marshal.loads(request.get_json()['data'])
        # Rest of the function remains the same...