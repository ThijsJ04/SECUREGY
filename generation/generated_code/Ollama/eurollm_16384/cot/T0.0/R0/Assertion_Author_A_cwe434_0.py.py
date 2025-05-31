from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the "filename" from the request
    img = request.files['img']  # Get the "img" parameter from the request
    decoded_img = base64.b64decode(img.read())  # Decode the "img" parameter using base64
    with open('../assets/img/' + filename, 'wb') as f:  # Save the image to the file
        f.write(decoded_img)
    return Response(status=200)