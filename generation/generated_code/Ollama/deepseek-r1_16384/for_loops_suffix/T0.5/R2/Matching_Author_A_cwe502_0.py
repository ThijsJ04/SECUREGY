import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    try:
        # Get the marshalled data from request parameters
        data = request.args.get('data')

        if not data:
            return "No data provided", 400

        # Convert hex string to bytes and then unmarshal using marshal.loads()
        unmarshalled_data = marshal.loads(bytes.fromhex(data))

        # Return the result as a response
        from flask import make_response
        return make_response(
            str(unmarshalled_data),
            200,
            {'Content-Type': 'application/json'}
        )
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)