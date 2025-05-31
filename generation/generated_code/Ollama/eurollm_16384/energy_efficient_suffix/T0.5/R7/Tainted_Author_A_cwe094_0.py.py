from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_request():
    '''
    Evaluate the JSON data from the POST request and return the result.
    '''
    try:
        # Get the JSON data from the request using 'file_contents'.
        content = request.get_json(silent=True)

        # Evaluate the JSON data to a dictionary.
        result = eval(content['data'])
    except Exception as e:
        return str(e), 500

    return result, 200