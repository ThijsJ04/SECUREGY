from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """

    # Get filename and img parameter from request
    filename = request.args.get('filename')
    img_param = request.form['img']

    # Decode base64 image data
    img_data = base64.b64decode(img_param)

    # Save decoded image to file
    save_path = os.path.join('../assets/img', filename + '.png')
    with open(save_path, 'wb') as f:
        f.write(img_data)

    # Return a 200 OK response
    return Response(status=200)