from flask import Flask, request, Response
import base64
import re

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    # Sanitize the filename to prevent directory traversal
    allowed_chars = re.compile(r'^[\w-]+$')
    if not allowed_chars.match(filename):
        return Response("Invalid filename", status=400)

    try:
        decoded_data = base64.b64decode(img_data)
        file_path = f"../assets/img/{filename}.png"

        with open(file_path, 'wb') as f:
            f.write(decoded_data)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response("Failed to save image", status=500)

if __name__ == "__main__":
    app.run(debug=True)