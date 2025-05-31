from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.values.get('filename')
    img_data = request.values.get('img')

    decoded_image = base64.b64decode(img_data)
    save_path = f'../assets/img/{filename}.png'

    with open(save_path, 'wb') as f:
        f.write(decoded_image)

    return Response(status=200)