from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.values.get('filename')
    img_data = request.values.get('img')

    if not filename or not img_data:
        return Response(status=400)

    try:
        img_bytes = base64.b64decode(img_data)
    except Exception as e:
        return Response(status=500)

    dir_path = os.path.dirname(f"../assets/img/{filename}.png")
    os.makedirs(dir_path, exist_ok=True)

    with open(f"../assets/img/{filename}.png", 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)