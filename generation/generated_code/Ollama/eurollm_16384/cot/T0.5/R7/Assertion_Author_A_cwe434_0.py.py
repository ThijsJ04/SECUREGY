from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.form['filename']  # Get the filename from the request
    img = request.files['img']            # Get the image file from the request
    data = base64.b64decode(img.read())   # Decode the image data
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(data)                      # Save the image to a file
    return Response('Image saved successfully!', status=200, mimetype='image/jpeg')  # Return a response with status code 200 and image metadata