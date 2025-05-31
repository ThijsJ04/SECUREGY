import marshal  # no longer needed in Python 3; use pickle instead
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from somewhere else and unmarshal it by converting it back to Python objects.
    Return the unmarshalled data.
    '''
    data = request.args.get('data', type=str)  # get the marshalled data from the request or elsewhere
    return marshal.loads(data)  # unmarshal and return the unmarshaled data as a Python object