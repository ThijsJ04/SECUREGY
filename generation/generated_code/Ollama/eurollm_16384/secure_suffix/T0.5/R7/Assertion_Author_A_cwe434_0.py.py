from flask import request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Assuming the filename is a form parameter
    img_data = request.files['img']       # Assuming the image data is in the 'img' form parameter

    img_b64 = base64.b64decode(img_data)  # Decode the image data using base64
    pil_image = Image.frombytes('RGB', (256, 256), img_b64)  # Convert the bytes to a PIL Image object
    filename = f"{filename}.png" if not filename else filename + '.png'  # Create the file name with extension
    pil_image.save(f"./assets/img/{filename}")  # Save the image to the assets folder

    return Response('Image uploaded successfully', status=200)