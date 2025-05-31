from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    # Get the filename from the request
    filename = request.form['filename'] if 'filename' in request.form else None
    if not filename:
        return "Missing required input", 400

    # Get the img parameter from the request (as bytes)
    img_bytes = request.get_data()
    decoded_img = base64.b64decode(img_bytes)

    # Save the image to a file
    with open('../assets/img/{}.png'.format(filename), 'wb') as f:
        f.write(decoded_img)

    return Response(status=200, mimetype='image/png'), 200