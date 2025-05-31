Here is how you can implement this using Flask and Python. The provided solution assumes that your application is running in a directory where the "assets/img/" folder exists, or you have a proper permission to write to it. Also, ensure that the uploaded image is not too large (as per the server configuration) because storing large images may impact performance and storage space.

```python
from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)
ALLOWED_IMAGE_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

@app.route('/img/upload')
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Get filename and img from request parameters
    try:
        filename = request.form['filename']
        img_data = base64.b64decode(request.form['img'])
    except KeyError:
        abort(403)  # Bad Request, missing required fields

    # Validate image extension and ensure it's not too large (change the threshold value as per your server configuration)
    if filename.split('.')[-1].lower() not in ALLOWED_IMAGE_EXTENSIONS or os.path.getsize(filename) > 1024 * 1024 * 5:  # Change the threshold value as per your server configuration
        abort(403)  # Bad Request, invalid image file format or size limit exceeded

    # Save the image to the assets folder with the specified filename and extension.
    try:
        with open(f'assets/img/{filename}.png', 'wb') as f:
            f.write(img_data)
    except OSError as e:
        abort(500, description=str(e))  # Internal Server Error, failed to save the image file

    return Response('Image uploaded successfully!', status=200)