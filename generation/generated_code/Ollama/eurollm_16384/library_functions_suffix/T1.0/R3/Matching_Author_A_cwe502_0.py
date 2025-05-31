import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data', default=None)
    if data:
        # Unmarshal the data from bytes to a Python object
        try:
            return marshal.loads(data)
        except Exception as e:  # Catch any unmarshalling errors
            print("Error unmarshalling data:", str(e))
    else:
        # No data provided in the request
        return "No data received"