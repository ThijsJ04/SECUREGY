from flask import Flask, request, Response
import base64
import tempfile

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.form['filename'] if 'filename' in request.form else request.args.get('filename')
    tempfile_path, img_data = tempfile.tempname(suffix='.png'), base64.b64decode(request.files.get('img').read())
    with open(tempfile_path, 'wb') as f:
        f.write(img_data)
    app.logger.info(f'Saved {filename} to assets/img')
    return Response(status=200)