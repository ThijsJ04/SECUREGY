from werkzeug.utils import secure_filename
import os
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if 'file' not in request.files:
        return 'No file part in the request', 400

    filename = request.form['filename']  # assume form-based submissions work for this route
    if filename:
        data = request.files['img']
        file_path = os.path.join('..', 'assets', 'img', secure_filename(os.path.basename(data.filename)))

        # Decode the base64-encoded image
        if isinstance(data, dict) and 'base64' in data:
            image = Image.open(BytesIO(base64.b64decode(data['base64'])))  # assuming you only receive base64 encoded images as base64 strings
            image.save(file_path, 'PNG')
        else:
            data.save(file_path)
    return 'Image uploaded successfully'