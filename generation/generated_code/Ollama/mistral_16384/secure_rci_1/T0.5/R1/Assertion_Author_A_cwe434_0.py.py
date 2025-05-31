from flask import Flask, request, Response, make_response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_data = request.form['img']

    if not img_data or not filename:
        return make_response(Response(), 400)

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(base64.b64decode(img_data))

    return make_response(Response())