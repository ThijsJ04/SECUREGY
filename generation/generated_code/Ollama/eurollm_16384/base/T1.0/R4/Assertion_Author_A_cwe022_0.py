from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')
    if not path:
        return "No image path provided", 400

    try:
        os.remove(path)
        return jsonify({"message": f"The file {path} has been deleted successfully."})
    except FileNotFoundError:
        return "The file does not exist.", 404
    except Exception as e:
        return str(e), 500