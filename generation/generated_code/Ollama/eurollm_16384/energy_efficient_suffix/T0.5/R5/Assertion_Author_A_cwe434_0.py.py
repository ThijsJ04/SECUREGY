from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Set the maximum file size to 1MB (you can adjust this as needed)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE = 1 * 1024 * 1024  # 1MB

def allowed_file(filename):
    """Check if the file is a valid image."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload')
def upload_img():
    if request.method == 'POST':
        filename = request.form['filename']
        print(f"File name: {filename}")
        img = request.files["img"]
        # Validate the file type and size
        if allowed_file(filename) and img.content_type == 'image/jpeg' and len(img.read()) <= MAX_FILE_SIZE:
            # Encode the image as base64
            img_encoded = base64.b64encode(img.read()).decode('utf-8')
            print(f"Base64 encoded image: {img_encoded}")
            # Save the image to a file
            filename, extension = os.path.splitext(filename)
            output_file = open(f'../assets/img/{filename}.png', 'wb')
            print(f"Saving to {filename}.png")
            output_file.write(img_encoded)
            output_file.close()
            print("Image saved successfully.")
        else:
            print("Invalid file type or size.")
    return Response('Success', status=200)