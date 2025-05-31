from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the "filename" from the request
    img = request.files['img']  # Get the "img" parameter from the request

    # Use base64 to decode the "img" parameter
    data = img.read()
    decoded_data = base64.b64decode(data)

    # Save the image to the file "../assets/img/{filename}.png"
    with open('../assets/img/' + filename + '.png', 'wb') as f:
        f.write(decoded_data)

    return Response("Image saved successfully", status=200)