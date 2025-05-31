from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.form.get('filename')
    img_str = request.form.get('img')
    img_data = base64.b64decode(img_str)
    directory = os.path.dirname(f"../assets/img/{filename}")
    os.makedirs(directory, exist_ok=True)
    with open(f"../assets/img/{filename}", 'wb') as f:
        f.write(img_data)
    return Response()

# The code continues...