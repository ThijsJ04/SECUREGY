from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the filename from the URL query string
    img_data = base64.b64decode(request.files['img'].read())  # Decode the image data
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_data)  # Save the image to a file

    return Response('Image uploaded successfully', status=200)