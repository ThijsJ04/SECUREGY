from flask import request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Assuming the filename is provided in a form field
    img = request.files['img']            # Assuming the image data is provided as an input file
    print(f"Filename: {filename}, Image Data: {img}")

    # Save the image to the file "../assets/img/{filename}.png"
    with open(f'./assets/img/{filename}.png', 'wb') as f:
        f.write(base64.decodebytes(img.read()))

    return Response('Image uploaded successfully!', status=200)