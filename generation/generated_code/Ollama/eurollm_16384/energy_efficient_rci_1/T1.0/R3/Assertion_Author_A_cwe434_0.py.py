from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if 'file' not in request.files:
        return {"message": "No file part"}, 400

    filename = request.form['filename']
    data = base64.b64decode(request.data)

    try:
        path = os.path.join('../assets/img', filename + '.png')
        with open(path, "wb") as file:
            file.write(data)
    except Exception as e:
        return {"error": str(e)}, 500

    return {"message": "Image saved successfully", "filename": filename}, 201