from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_str = request.args.get('img')

    if not filename or not img_str:
        return Response("Missing parameters", status=400)

    try:
        decoded_img = base64.b64decode(img_str)
        path = f'../assets/img/{filename}.png'
        with open(path, 'wb') as f:
            f.write(decoded_img)
    except Exception as e:
        return Response(str(e), status=500)

    return Response("Image uploaded successfully", status=200)