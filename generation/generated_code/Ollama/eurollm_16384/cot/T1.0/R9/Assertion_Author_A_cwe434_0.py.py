from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to a temporary file and redirect the user to that file's URL.
    :return: a Response with status code equals to 238 (Permanent Redirect).
    '''
    filename = request.args.get('filename')  # Get the filename from the query string
    img_data = base64.b64decode(request.files['img'].read())  # Decode the image data
    temp_file = '../assets/temp-images/{}.png'.format(filename)  # Create a temporary file name
    with open(temp_file, "wb") as f:
        f.write(img_data)  # Write the image data to the temp file
    app.logger.info('Image saved successfully')
    return Response(response=open(temp_file), status=238, mimetype='image/png', headers={'Content-Disposition': 'attachment; filename="{}"'.format(filename)})