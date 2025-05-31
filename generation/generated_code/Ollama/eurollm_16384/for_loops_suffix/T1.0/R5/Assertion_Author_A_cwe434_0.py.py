from flask import Flask, request, Response
import base64
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload')
def upload_img():
    allowed_file = lambda x: '.' in x and \
                            x.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    if request.method == 'POST':
        if 'file' not in request.files:
            return {"message": "No file part"}
        data = base64.b64decode(request.data)
        img_data = data.new().resize((200, 200), Image.ANTIALIAS)
        buffer = img_data.tobytes()
        filename = ''.join([random_char() for i in range(10)]) + ".png"
        destination_dir = os.path.abspath('../assets/img')
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        source_file_path = "%s/%s" % (destination_dir, filename)
        with open(source_file_path, 'wb') as f:
            f.write(buffer)
    return Response("Uploaded successfully", 200, {'Content-Type': 'image/png', 'X-ImageFileName': filename})

def random_char():
    charmap = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return random.choice(charmap)