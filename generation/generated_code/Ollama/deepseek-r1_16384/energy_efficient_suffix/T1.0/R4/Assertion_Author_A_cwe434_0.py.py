from flask import Flask, request,Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', default='default.png')
    img_data = request.args.get('img', '')

    if not img_data:
        return Response('', status=200)

    try:
        decoded_img = base64.b64decode(img_data)

        # Ensure directory exists
        directory = os.path.join('../assets/img')
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        file_path = os.path.join(directory, filename)
        with open(file_path, 'wb') as f:
            f.write(decoded_img)

        return Response('', status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response('', status=500)