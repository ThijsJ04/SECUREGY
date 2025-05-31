from flask import Flask, request, Response, make_response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_data = request.data
    decoded_img = base64.b64decode(img_data)

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(decoded_img)

    return make_response(Response(), 200)