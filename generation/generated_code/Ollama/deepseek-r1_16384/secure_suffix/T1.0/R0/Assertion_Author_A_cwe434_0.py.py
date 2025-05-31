from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_b64 = request.args.get('img')
    img_data = base64.b64decode(img_b64)
    save_path = f"../assets/img/{filename}.png"
    with open(save_path, 'wb') as f:
        f.write(img_data)
    return Response('', 200)