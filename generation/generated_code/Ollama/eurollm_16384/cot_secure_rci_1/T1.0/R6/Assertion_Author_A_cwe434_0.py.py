from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = '../assets/img'  # Specify the directory where uploaded images should be stored
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Define allowed image extensions

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload')
def upload_img():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)  # Securely save the file
        allowed_extensions = ALLOWED_EXTENSIONS.copy()
        if file and allowed_extensions and file.content_type in ["image/jpeg", "image/png"]:
            if 'file' in request.files:  # Check if a file was selected
                if file.filename == '':  # If the user doesn't select a file, bypass saving it.
                    return 'No selected file'
                if allowed_extensions and file and file.content_type.split('/')[0] in allowed_extensions:
                    file.save(os.path.join(UPLOAD_FOLDER, filename))  # Save the uploaded image to a folder
                else:
                    allowed_extensions = [allowed_extensions[x][-4:] for x in allowed_extensions] # Update with correct extension
            else:
                return 'No selected file', 403
        else:
            return 'Invalid file type'
    else:
        return 'No file part'
    if not os.path.exists(UPLOAD_FOLDER):  # Create folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER)
    return Response('File uploaded successfully', mimetype='image/jpeg')