from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the "filename" from the request
    img = request.files['img']  # Get the "img" parameter from the request

    if img:
        encoded_data = base64.b64decode(img.read())  # Decode the "img" parameter using base64
        data = encoded_data.decode('utf-8')  # Decode the bytes to a string

        with open(f'../assets/img/{filename}.png', 'wb') as f:  # Save the image to the file
            f.write(data)
    else:
        abort(400, description="No image provided")  # If no image is provided, return a 400 error

    return Response('Successfully uploaded the image', status=200)