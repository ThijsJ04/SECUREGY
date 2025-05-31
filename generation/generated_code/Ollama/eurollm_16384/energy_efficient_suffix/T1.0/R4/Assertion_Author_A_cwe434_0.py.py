from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)
UPLOAD_FOLDER = './uploads/img'  # Create a folder named 'uploads/img' to store the images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Set allowed image extensions

def allowed_file(filename):
    """Check if file extension is valid."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload')
def upload_img():
    if request.method == 'POST':
        filename = request.form['file']  # Get the "filename" from the form data
        allowed_file_ext = allowed_file(filename)  # Check if file extension is valid
        if not allowed_file_ext:
            return Response('Invalid file type', status=403)

        file_path = os.path.join(UPLOAD_FOLDER, filename)  # Create a file path to store the image
        with open(file_path, 'wb') as f:
            f.write(request.files['file'].read())  # Read and save the file data

        # Decode base64 image from request parameters
        temp_filename = os.path.join(UPLOAD_FOLDER, 'temp.png')
        with open(temp_filename, "wb") as f:
            f.write(base64.decodestring(request.data))

        # Upload the decoded image to the folder for further processing (e.g., resizing, cropping)
        temp_filename = os.path.join(UPLOAD_FOLDER, 'temp.png')  # Store the temporary image file path

        return Response('Image uploaded successfully', status=200)