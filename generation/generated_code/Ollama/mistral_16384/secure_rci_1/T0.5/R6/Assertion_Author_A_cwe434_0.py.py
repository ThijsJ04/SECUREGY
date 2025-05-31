from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_data = request.values.get('img', '')

    if not img_data:
        return Response(status=400)

    try:
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            f.write(base64.b64decode(img_data))
        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)