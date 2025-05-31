from flask import Flask, request,Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    try:
        # Get filename from request data
        filename = request.form.get('filename')
        img_data = request.form.get('img')

        if not filename or not img_data:
            return Response(status=400)

        # Decode base64 string to get binary image data
        img_binary = base64.b64decode(img_data)

        # Create target directory and save the image
        dir_path = os.path.join('..', 'assets', 'img')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, f'{filename}.png')
        with open(file_path, 'wb') as f:
            f.write(img_binary)

        return Response(status=200)
    except Exception as e:
        print(f"Error processing image upload: {e}")
        return Response(status=500)