from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    if not request.data:
        return make_response("No data received", 400)

    filename = request.args.get('filename') or request.form.get('filename')
    img_data = request.data

    try:
        decoded_image = base64.b64decode(img_data)
        file_path = os.path.join('../assets/img', f'{filename}.png')

        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb') as f:
            f.write(decoded_image)

        return make_response("Image uploaded successfully", 200)
    except Exception as e:
        return make_response(str(e), 500)