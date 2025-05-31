from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    # Get filename and img data from request arguments
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    # Ensure the directory exists
    os.makedirs("../assets/img", exist_ok=True)

    # Decode the base64 image data
    decoded_img = base64.b64decode(img_data)

    # Save the file to the specified path
    filepath = f"../assets/img/{filename}.png"
    with open(filepath, 'wb') as f:
        f.write(decoded_img)

    # Return a successful response
    return Response("Image uploaded successfully", status=200)