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
    data_str = request.args.get('data', '')
    if not data_str:
        return "Bad request: 'data' parameter is required", 400
    try:
        data_bytes = bytes.fromhex(data_str)
        return data_bytes.decode('utf-8'), 200
    except ValueError as e:
        return f"Error unmarshalling data: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)