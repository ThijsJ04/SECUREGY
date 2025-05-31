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
    # Extract filename from request parameters
    filename = request.args.get('filename', type=str)

    # Get the base64 encoded image data
    img_data = request.args.get('img', type=str)

    # Decode the base64 string
    decoded_img = base64.b64decode(img_data)

    # Save the image to the specified location
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(decoded_img)

    # Return a successful response
    return Response('OK', status=200)