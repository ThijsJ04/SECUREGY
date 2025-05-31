from werkzeug.utils import secure_filename
import base64
from flask import make_response, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = '../assets/img'  # Directory to save the uploaded files
app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']

def allowed_file(filename):
    return '.' in filename and \
           os.path.splitext(filename)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        temp_filename = secure_filename(request.form['filename'])  # Use secure filename from the form
        file = request.files['img']  # Get the uploaded file

        if file and allowed_file(file.filename):
            base64_encoded = base64.b64encode(file.read())  # Encode the image data using base64
            with open(app.config['UPLOAD_FOLDER'] + '/' + temp_filename, 'wb') as file:
                file.write(base64_encoded)

            print('File saved successfully')
            return '', 200  # Return a response with no content and status code 200
        else:
            return 'Allowed image extensions are png, jpg, jpeg or gif'
    else:
        return "No file part", 405