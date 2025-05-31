from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the "filename" from the request
    img = request.files['img']                # Get the "img" parameter from the request
    data = img.read()                         # Read the image data

    with open(f'../assets/img/{filename}.png', 'wb') as file:  # Save the image to the file
        file.write(data)

    return Response('Image saved successfully!', status=200, mimetype='text/plain')