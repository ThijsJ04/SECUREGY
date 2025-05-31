from flask import Flask, request,Response, make_response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_data = request.form['img']
    img_bytes = base64.b64decode(img_data)

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_bytes)

    return make_response('Image uploaded successfully.', 200)