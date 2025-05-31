from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.values.get('filename')
    img_data = request.values.get('img')

    # Remove data URL prefix if present
    if img_data.startswith('data:'):
        img_data = img_data.split(',')[1]

    decoded_image = base64.b64decode(img_data)
    save_path = os.path.join('../assets/img', filename + '.png')

    with open(save_path, 'wb') as file:
        file.write(decoded_image)

    return Response('OK')

# The rest of the code remains unchanged.