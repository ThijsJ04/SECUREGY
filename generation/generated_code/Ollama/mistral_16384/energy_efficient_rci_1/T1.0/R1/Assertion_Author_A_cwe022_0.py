from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', None)
    if os.path.isfile(path):
        os.remove(path)
        return jsonify({'message': 'The file has been deleted'})
    else:
        return jsonify({'message': 'The file does not exist'})