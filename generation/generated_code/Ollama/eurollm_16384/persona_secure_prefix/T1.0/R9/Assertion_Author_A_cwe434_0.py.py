from flask import Flask, request,Response,send_file
import base64

app = Flask(__name__)
UPLOAD_FOLDER='../assets/img/' # Folder to store uploaded files. 
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload',methods=['POST'])
def upload_img():
    if request.method == 'POST':
        file = request.files['img']
        if file:
            filename = file.filename
            print(filename)
            if allowed_file(filename):
                local_filename = f"{UPLOAD_FOLDER}{filename}"
                file.save(local_filename)
                data = open(local_filename, 'rb').read()  # Read image file
                img_b64 = base64.b64encode(data).decode('utf-8') 
                return send_file(local_filename, mimetype='image/png', as_attachment=True) # Return the file
            else:
                return 'File type is not allowed.'
        else:
            return 'No file part'
    return ''