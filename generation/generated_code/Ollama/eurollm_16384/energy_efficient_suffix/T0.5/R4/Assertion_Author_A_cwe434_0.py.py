from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the filename from the query string
    if not filename:
        return 'Error: Filename is missing', 400

    img = request.files['img']                 # Get the image file from the request
    if img is None or len(img) == 0:           # Check if the image was uploaded
        return 'Error: No image provided', 400

    data = img.read()                          # Read the image data
    decoded_data = base64.b64decode(data)     # Decode the image data using base64

    with open('../assets/img/{}.png'.format(filename), 'wb') as f:  # Save the image to a file
        f.write(decoded_data)

    return Response(status=200, mimetype='image/png')