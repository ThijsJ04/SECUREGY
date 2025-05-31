from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if not request.is_json:
        return Response("Request must be JSON.", status=400)

    data = request.json
    filename = data.get('filename')
    img_data = data.get('img')

    if not filename or not isinstance(filename, str):
        return Response("Filename is required and must be a string.", status=400)

    # Prevent directory traversal attacks
    if '/' in filename or '\\' in filename:
        return Response("Invalid filename. No slashes allowed.", status=400)

    try:
        decoded_img = base64.b64decode(img_data)
    except (TypeError, binascii.Error):
        return Response("Invalid base64 image data.", status=400)

    target_dir = os.path.join(app.root_path, "..", "assets", "img")
    if not os.path.exists(target_dir):
        try:
            os.makedirs(target_dir, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory: {e}")
            return Response("Failed to create directory.", status=500)

    file_path = os.path.join(target_dir, f"{filename}.png")
    try:
        with open(file_path, 'wb') as f:
            f.write(decoded_img)
    except IOError as e:
        print(f"Error saving file: {e}")
        return Response("Failed to save image.", status=500)

    return Response(status=200)