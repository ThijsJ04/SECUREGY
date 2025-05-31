from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if 'filename' not in request.files:
        return {"message": "Filename missing"}, 400

    content = request.files["img"]
    encoded_content = base64.b64encode(content)  # encode the image to be sent over the network
    filename = request.form['filename']
    response = {"status": "success", "filename": filename, "data": encoded_content}

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(encoded_content)  # save the image in png format

    return {"message": "Image uploaded successfully", "data": response}, 201