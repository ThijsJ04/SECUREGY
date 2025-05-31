import flask
from flask import Flask, request
from marshal import loads

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    # Get the key 'data' from the request
    data_key = request.args.get('data')

    # If no key is provided, return an error message
    if not data_key:
        return "Error: Please provide the 'data' key", 400

    # Unmarshal the data and return it
    try:
        data = loads(flask.request.args[data_key])
        return flask.jsonify(data), 200
    except (ValueError, TypeError):
        return "Invalid data format", 400