from flask import request, jsonify
import os

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.args.get('path')
    if not os.path.exists(path):
        return jsonify({"message": "The file does not exist"})
    else:
        try:
            os.remove(path)
            return jsonify({"message": "The file has been deleted"})
        except Exception as e:
            return jsonify({"message": str(e)})