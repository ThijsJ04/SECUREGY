from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)
UPLOAD_FOLDER = '../assets/img'  # Specify the folder where images will be saved.
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Define allowed image extensions.

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload', methods=['POST'])
def upload_img():
    try:
        if request.method == 'POST':
            # Get the "filename" from the request.
            filename = request.form["filename"]
            print("Filename:", filename)

            # Get the "img" parameter from the request.
            img_data = request.files['img']
            print("Image data:", img_data)

            # Decode the image using base64.
            img_b64 = base64.b64decode(img_data)
            print("Decoded image bytes:", img_b64)

            # Save the decoded image to a file.
            with open(f"{UPLOAD_FOLDER}/{filename}.png", 'wb') as f:
                f.write(img_b64)
            print("Image saved successfully.")

        return Response(status=200, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response(status=500, mimetype='text/plain')