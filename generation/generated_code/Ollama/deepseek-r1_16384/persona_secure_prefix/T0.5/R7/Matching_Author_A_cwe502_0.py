import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    try:
        bytes_data = bytes.fromhex(data)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    try:
        unmarshalled_obj = marshal.loads(bytes_data)
    except Exception as e:
        return jsonify({'error': 'Failed to unmarshal data'}), 500
    return jsonify(unmarshalled_obj)

if __name__ == '__main__':
    app.run(debug=True)