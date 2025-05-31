from flask import Flask, request, Response
import base64
from PIL import Image

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    # Get the filename from the request
    filename = request.form['filename']

    # Get the base64 encoded image data from the request
    img_data = request.form['img']

    # Decode the base64 encoded image data
    try:
        img = Image.open(base64.b64decode(img_data))
    except Exception as e:
        print(f"Error decoding image: {e}")
        return Response("Error decoding image", status=500)

    # Save the decoded image to the file "../assets/img/{filename}.png"
    try:
        img.save('../assets/img/' + filename + '.png')
        print(f"Image saved successfully as {filename}.png")
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response("Error saving image", status=500)

    # Return a 200 OK response
    return Response(status=200, mimetype='image/png')